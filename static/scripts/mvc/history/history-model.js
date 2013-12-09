//define([
//    "../mvc/base-mvc"
//], function(){
//==============================================================================
/** @class Model for a Galaxy history resource - both a record of user
 *      tool use and a collection of the datasets those tools produced.
 *  @name History
 *
 *  @augments Backbone.Model
 *  @borrows LoggableMixin#logger as #logger
 *  @borrows LoggableMixin#log as #log
 *  @constructs
 */
var History = Backbone.Model.extend( LoggableMixin ).extend(
/** @lends History.prototype */{
    //TODO: bind change events from items and collection to this (itemLengths, states)

    ///** logger used to record this.log messages, commonly set to console */
    //// comment this out to suppress log output
    //logger              : console,

    // values from api (may need more)
    defaults : {
        id              : null,
        name            : 'Unnamed History',
        state           : 'new',

        diskSize : 0,
        deleted : false
    },

    //TODO: hardcoded
    urlRoot: 'api/histories/',
    /** url for fetch */
    url : function(){
        // api location of history resource
        return this.urlRoot + this.get( 'id' );
    },

    /** Set up the hdas collection
     *  @param {Object} initialSettings model data for this History
     *  @param {Object[]} initialHdas array of model data for this History's HDAs
     *  @see BaseModel#initialize
     */
    initialize : function( initialSettings, initialHdas, logger ){
        logger = logger || null;
        this.log( this + ".initialize:", initialSettings, initialHdas );

        /** HDACollection of the HDAs contained in this history. */
        this.hdas = new HDACollection();

        // if we've got hdas passed in the constructor, load them and set up updates if needed
        if( initialHdas && _.isArray( initialHdas ) ){
            this.hdas.reset( initialHdas );
            this.checkForUpdates();
            //TODO: don't call if force_history_refresh
            if( this.hdas.length > 0 ){
                this.updateDisplayApplications();
            }
        }

        // if an hda moves into the ready state and has the force_history_refresh flag (often via tool.xml)
        //  then: refresh the panel
        this.hdas.bind( 'state:ready', function( hda, newState, oldState ){
            if( hda.get( 'force_history_refresh' ) ){
                //TODO: could poll jobs here...
                var history = this;
                setTimeout( function(){
                    history.stateUpdater();
                }, History.UPDATE_DELAY );
            }
        }, this );

        if( this.logger ){
            this.bind( 'all', function( event ){
                this.log( this + '', arguments );
            }, this );
        }
    },

    // reduce the state_ids map of hda id lists -> a single list of ids
    //...ugh - seems roundabout; necessary because the history doesn't have a straightforward list of ids
    //  (and history_contents/index curr returns a summary only)
    hdaIdsFromStateIds : function(){
        return _.reduce( _.values( this.get( 'state_ids' ) ), function( reduction, currIdList ){
            return reduction.concat( currIdList );
        });
    },

    // get the history's state from it's cummulative ds states, delay + update if needed
    // events: ready
    checkForUpdates : function(){
        // get overall History state from collection, run updater if History has running/queued hdas
        // boiling it down on the client to running/not
        if( this.hdas.running().length ){
            this.stateUpdater();

        } else {
            this.trigger( 'ready' );
        }
        return this;
    },

    // update this history, find any hda's running/queued, update ONLY those that have changed states,
    //  set up to run this again in some interval of time
    // events: ready
    stateUpdater : function(){
        var history = this,
            oldState = this.get( 'state' ),
            // state ids is a map of every possible hda state, each containing a list of ids for hdas in that state
            oldStateIds = this.get( 'state_ids' );

        // pull from the history api
        //TODO: fetch?
        jQuery.ajax( 'api/histories/' + this.get( 'id' )

        ).success( function( response ){
            //this.log( 'historyApiRequest, response:', response );
            history.set( response );
            history.log( 'current history state:', history.get( 'state' ),
                '(was)', oldState,
                'new size:', history.get( 'nice_size' ) );

            //TODO: revisit this - seems too elaborate, need something straightforward
            // for each state, check for the difference between old dataset states and new
            //  the goal here is to check ONLY those datasets that have changed states (not all datasets)
            var changedIds = [];
            _.each( _.keys( response.state_ids ), function( state ){
                var diffIds = _.difference( response.state_ids[ state ], oldStateIds[ state ] );
                // aggregate those changed ids
                changedIds = changedIds.concat( diffIds );
            });

            // send the changed ids (if any) to dataset collection to have them fetch their own model changes
            if( changedIds.length ){
                history.fetchHdaUpdates( changedIds );
            }

            // set up to keep pulling if this history in run/queue state
            if( ( history.get( 'state' ) === HistoryDatasetAssociation.STATES.RUNNING )
            ||  ( history.get( 'state' ) === HistoryDatasetAssociation.STATES.QUEUED ) ){
                setTimeout( function(){
                    history.stateUpdater();
                }, History.UPDATE_DELAY );

            // otherwise, we're now in a 'ready' state (no hdas running)
            } else {
                history.trigger( 'ready' );
            }

        }).error( function( xhr, status, error ){
            //TODO: use ajax.status handlers here
            // keep rolling on a bad gateway - server restart
            if( xhr.status === 502 ){
                setTimeout( function(){
                    history.log( 'Bad Gateway error. Retrying...' );
                    //TODO: someway to throw error on X tries
                    history.stateUpdater();
                }, History.UPDATE_DELAY );

            // if not interruption by iframe reload
            //TODO: remove when iframes are removed
            } else if( !( ( xhr.readyState === 0 ) && ( xhr.status === 0 ) ) ){
                history.log( 'stateUpdater error:', error, 'responseText:', xhr.responseText );
                var msg = _l( 'An error occurred while getting updates from the server.' ) + ' '
                        + _l( 'Please contact a Galaxy administrator if the problem persists.' );
                history.trigger( 'error', msg, xhr, status, error );
            }
        });
    },

    /** Update the models in the hdas collection that match the ids given by getting their data
     *      via the api/AJAX. If a model exists in the collection, set will be used with the new data.
     *      If it's not in the collection, addHdas will be used to create it.
     *  @param {String[]} hdaIds an array of the encoded ids of the hdas to get from the server.
     */
    fetchHdaUpdates : function( hdaIds ){
        //TODO:?? move to collection? still need proper url
        var history = this;
        jQuery.ajax({
            url     : this.url() + '/contents?' + jQuery.param({ ids : hdaIds.join(',') }),

            /**
             *  @inner
             */
            error   : function( xhr, status, error ){
                if( ( xhr.readyState === 0 ) && ( xhr.status === 0 ) ){ return; }

                var errorJson = JSON.parse( xhr.responseText );
                if( _.isArray( errorJson ) ){

                    // just for debugging/reporting purposes
                    var grouped = _.groupBy( errorJson, function( hdaData ){
                        if( _.has( hdaData, 'error' ) ){ return 'errored'; }
                        return 'ok';
                    });
                    history.log( 'fetched, errored datasets:', grouped.errored );

                    // the server already formats the error'd hdas in proper hda-model form
                    //  so we're good to send these on
                    history.updateHdas( errorJson );

                } else {
                    history.log( 'Error updating hdas from api history contents',
                        hdaIds, xhr, status, error, errorJson );
                    var msg = _l( 'An error occurred while getting dataset details from the server.' ) + ' '
                            + _l( 'Please contact a Galaxy administrator if the problem persists.' );
                    history.trigger( 'error', msg, xhr, status, error );
                }
            },

            /** when the proper models for the requested ids are returned,
             *      either update existing or create new entries in the hdas collection
             *  @inner
             */
            success : function( hdaDataList, status, xhr ){
                history.log( history + '.fetchHdaUpdates, success:', status, xhr );
                history.updateHdas( hdaDataList );
            }
        });
    },

    /** Update the models in the hdas collection from the data given.
     *      If a model exists in the collection, set will be used with the new data.
     *      If it's not in the collection, addHdas will be used to create it.
     *  @param {Object[]} hdaDataList an array of the model data used to update.
     */
    updateHdas : function( hdaDataList ){
        var history = this,
            // models/views that need to be created
            hdasToAdd = [];
        history.log( history + '.updateHdas:', hdaDataList );

        _.each( hdaDataList, function( hdaData, index ){
            var existingModel = history.hdas.get( hdaData.id );
            // if this model exists already, update it
            if( existingModel ){
                history.log( 'found existing model in list for id ' + hdaData.id + ', updating...:' );
                existingModel.set( hdaData );

            // if this model is new and isn't in the hda collection, cache it to be created
            } else {
                history.log( 'NO existing model for id ' + hdaData.id + ', creating...:' );
                hdasToAdd.push( hdaData );
            }
        });
        if( hdasToAdd.length ){
            history.addHdas( hdasToAdd );
        }
    },

    /** Add multiple hda models to the hdas collection from an array of hda data.
     */
    addHdas : function( hdaDataList ){
        //TODO: this is all probably easier if hdas is a relation
        var history = this;
        //TODO:?? what about hidden? deleted?
        _.each( hdaDataList, function( hdaData, index ){
            var indexFromHid = history.hdas.hidToCollectionIndex( hdaData.hid );
            hdaData.history_id = history.get( 'id' );
            history.hdas.add( new HistoryDatasetAssociation( hdaData ), { at: indexFromHid, silent: true });
        });
        // fire only once
        history.hdas.trigger( 'add', hdaDataList );
    },

    /** Update (from controller) the display application link data of the hdas with the given ids.
     *  @param {String[]} ids an array of hda ids to update (optional, defaults to all hdas)
     *  @returns {HistoryDatasetAssociation[]} hda models that were updated
     */
    updateDisplayApplications : function( ids ){
        this.log( this + 'updateDisplayApplications:', ids );
        var history = this,
        //    data = { id: this.get( 'id' ) };
        //if( ids && _.isArray( ids ) ){ data.hda_ids = ids.join( ',' ); }
            data = ( ids && _.isArray( ids ) )?({ hda_ids : ids.join( ',' ) }):({});

        //TODO: hardcoded
        history.log( this + ': fetching display application data' );
        jQuery.ajax( 'history/get_display_application_links', {
            data : data,
            success : function( data, status, xhr ){
                history.hdas.set( data );
            },
            error : function( xhr, status, error ){
                if( !( ( xhr.readyState === 0 ) && ( xhr.status === 0 ) ) ){
                    history.log( 'Error fetching display applications:', ids, xhr, status, error );
                    var msg = _l( 'An error occurred while getting display applications from the server.' ) + ' '
                            + _l( 'Please contact a Galaxy administrator if the problem persists.' );
                    history.trigger( 'error', msg, xhr, status, error );
                }
            }
        });
    },

    toString : function(){
        var nameString = ( this.get( 'name' ) )?
            ( ',' + this.get( 'name' ) ) : ( '' );
        return 'History(' + this.get( 'id' ) + nameString + ')';
    }
});

//------------------------------------------------------------------------------ CLASS VARS
/** When the history has running hdas,
 *  this is the amount of time between update checks from the server
 */
History.UPDATE_DELAY = 4000;


//==============================================================================
/** @class A collection of histories (per user).
 *      (stub) currently unused.
 *  @name HistoryCollection
 *
 *  @borrows LoggableMixin#logger as #logger
 *  @borrows LoggableMixin#log as #log
 *  @constructs
 */
var HistoryCollection = Backbone.Collection.extend( LoggableMixin ).extend(
/** @lends HistoryCollection.prototype */{
    model   : History,
    urlRoot : 'api/histories'
    
    ///** logger used to record this.log messages, commonly set to console */
    //// comment this out to suppress log output
    //logger              : console,
});

//==============================================================================
//return {
//    History           : History,
//    HistoryCollection : HistoryCollection,
//};});
