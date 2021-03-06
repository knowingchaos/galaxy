// have to handle errors here - or phantom/casper won't bail but _HANG_
try {
    var utils = require( 'utils' ),
        xpath = require( 'casper' ).selectXPath,
        format = utils.format,

        //...if there's a better way - please let me know, universe
        scriptDir = require( 'system' ).args[3]
            // remove the script filename
            .replace( /[\w|\.|\-|_]*$/, '' )
            // if given rel. path, prepend the curr dir
            .replace( /^(?!\/)/, './' ),
        spaceghost = require( scriptDir + 'spaceghost' ).create({
            // script options here (can be overridden by CLI)
            //verbose: true,
            //logLevel: debug,
            scriptDir: scriptDir
        });

    spaceghost.start();

} catch( error ){
    console.debug( error );
    phantom.exit( 1 );
}

// ===================================================================
/* TODO:
    possibly break this file up
*/
// =================================================================== globals and helpers
var email = spaceghost.user.getRandomEmail(),
    password = '123456';
if( spaceghost.fixtureData.testUser ){
    email = spaceghost.fixtureData.testUser.email;
    password = spaceghost.fixtureData.testUser.password;
    spaceghost.info( 'Will use fixtureData.testUser: ' + email );
}

// selectors and labels
var tooltipSelector     = spaceghost.data.selectors.tooltipBalloon,
    editableTextClass   = spaceghost.data.selectors.editableText,
    editableTextInput   = spaceghost.data.selectors.editableTextInput,

    nameSelector     = spaceghost.historypanel.data.selectors.history.name,
    subtitleSelector = spaceghost.historypanel.data.selectors.history.subtitle,
    unnamedName      = spaceghost.historypanel.data.text.history.newName,
    initialSizeStr   = spaceghost.historypanel.data.text.history.newSize,
    tagIconSelector  = spaceghost.historypanel.data.selectors.history.tagIcon,
    annoIconSelector = spaceghost.historypanel.data.selectors.history.annoIcon,
    emptyMsgSelector = spaceghost.historypanel.data.selectors.history.emptyMsg,
    emptyMsgStr      = spaceghost.historypanel.data.text.history.emptyMsg,
    wrapperOkClassName  = spaceghost.historypanel.data.selectors.hda.wrapper.stateClasses.ok,
    tagAreaSelector     = spaceghost.historypanel.data.selectors.history.tagArea,
    annoAreaSelector    = spaceghost.historypanel.data.selectors.history.annoArea,
    nameTooltip      = spaceghost.historypanel.data.text.history.tooltips.name,

    refreshButtonSelector       = 'a#history-refresh-button',
    refreshButtonIconSelector   = 'span.fa-icon-refresh',
    refreshButtonHref           = '/history',

    includeDeletedOptionsLabel = spaceghost.historyoptions.data.labels.options.includeDeleted;

// local
var newHistoryName = "Test History",
    filepathToUpload = '../../test-data/1.txt',
    historyFrameInfo = {},
    testUploadInfo = {};


// =================================================================== TESTS
// ------------------------------------------------------------------- set up
// start a new user
spaceghost.user.loginOrRegisterUser( email, password );

// ------------------------------------------------------------------- check structure of empty history
spaceghost.thenOpen( spaceghost.baseUrl ).historypanel.waitForHdas( function(){
    this.test.comment( 'history panel with a new, empty history should be well formed' );
    this.test.comment( "frame should have proper url and title: 'History'" );
    this.test.assertMatch( this.getCurrentUrl(), /\/history/, 'Found history frame url' );
    this.test.assertTitle( this.getTitle(), 'History', 'Found history frame title' );

    this.test.comment( "history name should exist, be visible, and have text " + unnamedName );
    this.test.assertExists( nameSelector, nameSelector + ' exists' );
    this.test.assertVisible( nameSelector, 'History name is visible' );
    this.test.assertSelectorHasText( nameSelector, unnamedName, 'History name is ' + unnamedName );

    this.test.comment( "history subtitle should display size and size should be: " + initialSizeStr );
    this.test.assertExists( subtitleSelector, 'Found ' + subtitleSelector );
    this.test.assertVisible( subtitleSelector, 'History subtitle is visible' );
    this.test.assertSelectorHasText( subtitleSelector, initialSizeStr,
        'History subtitle has "' + initialSizeStr + '"' );

    this.test.comment( "tags and annotation icons should be available" );
    this.test.assertExists( tagIconSelector,  'Tag icon button found' );
    this.test.assertExists( annoIconSelector, 'Annotation icon button found' );

    this.test.comment( "A message about the current history being empty should be displayed" );
    this.test.assertExists( emptyMsgSelector, emptyMsgSelector + ' exists' );
    this.test.assertVisible( emptyMsgSelector, 'Empty history message is visible' );
    this.test.assertSelectorHasText( emptyMsgSelector, emptyMsgStr,
        'Message contains "' + emptyMsgStr + '"' );
});

// ------------------------------------------------------------------- name editing
spaceghost.withHistoryPanel( function(){
    this.test.comment( 'history panel, editing the history name' );

    this.test.comment( 'name should have a tooltip with proper info on name editing' );
    this.historypanel.hoverOver( nameSelector );
    this.test.assertExists( tooltipSelector, "Found tooltip after name hover" );
    this.test.assertSelectorHasText( tooltipSelector, nameTooltip );
    // clear the tooltip
    this.page.sendEvent( 'mousemove', -1, -1 );

    this.test.comment( 'name should be create an input when clicked' );
    this.assertHasClass( nameSelector, editableTextClass, "Name field classed for editable text" );
    this.click( nameSelector );
    this.test.assertExists( editableTextInput, "Clicking on name creates an input" );

    this.test.comment( 'name should be editable by entering keys and pressing enter' );
    //NOTE: casperjs.sendKeys adds a click before and a selector.blur after sending - won't work here
    this.page.sendEvent( 'keypress', newHistoryName );
    this.page.sendEvent( 'keypress', this.page.event.key.Enter );
    // wait for send and re-render name
    this.wait( 1000, function(){
        this.test.assertSelectorHasText( nameSelector, newHistoryName, 'History name is ' + newHistoryName );
        this.test.assertDoesntExist( editableTextInput, "Input disappears after pressing enter" );
    });
});

spaceghost.withHistoryPanel( function(){
    this.test.comment( 'name should revert if user clicks away while editing' );

    this.click( nameSelector );
    this.page.sendEvent( 'keypress', "Woodchipper metagenomics, Fargo, ND" );

    this.page.sendEvent( 'mousedown', -1, -1 );
    this.wait( 1000, function(){
        this.test.assertSelectorHasText( nameSelector, newHistoryName, 'History name is STILL ' + newHistoryName );
        this.test.assertDoesntExist( editableTextInput, "Input disappears after clicking away" );
    });
});

spaceghost.withHistoryPanel( function(){
    this.test.comment( 'name should revert if user hits ESC while editing' );

    this.click( nameSelector );
    this.page.sendEvent( 'keypress', "Arsenic Bacteria" );

    this.page.sendEvent( 'keypress', this.page.event.key.Escape );
    this.wait( 1000, function(){
        this.test.assertSelectorHasText( nameSelector, newHistoryName, 'History name is STILL ' + newHistoryName );
        this.test.assertDoesntExist( editableTextInput, "Input disappears after hitting ESC" );
    });
});

// ------------------------------------------------------------------- check structure of NON empty history
// upload file: 1.txt
spaceghost.tools.uploadFile( filepathToUpload, function uploadCallback( _uploadInfo ){
    this.test.comment( 'uploaded file should appear in history' );

    this.debug( 'uploaded HDA info: ' + this.jsonStr( _uploadInfo ) );
    var hasHda = _uploadInfo.hdaElement,
        hasClass = _uploadInfo.hdaElement.attributes[ 'class' ],
        hasOkClass = _uploadInfo.hdaElement.attributes[ 'class' ].indexOf( wrapperOkClassName ) !== -1;
    this.test.assert( ( hasHda && hasClass && hasOkClass ), "Uploaded file: " + _uploadInfo.name );
    testUploadInfo = _uploadInfo;
});

spaceghost.withHistoryPanel( function checkPanelStructure(){
    this.test.comment( 'checking structure of non-empty panel' );

    this.test.comment( "history name should exist, be visible, and have text " + unnamedName );
    this.test.assertExists( nameSelector, nameSelector + ' exists' );
    this.test.assertVisible( nameSelector, 'History name is visible' );
    this.test.assertSelectorHasText( nameSelector, newHistoryName, 'History name is ' + newHistoryName );

    this.test.comment( "history subtitle should display size and size should be " + onetxtFilesize + " bytes" );
    var onetxtFilesize = require( 'fs' ).size( this.options.scriptDir + filepathToUpload ),
        expectedSubtitle = onetxtFilesize + ' bytes';
    this.test.assertExists( subtitleSelector, 'Found ' + subtitleSelector );
    this.test.assertVisible( subtitleSelector, 'History subtitle is visible' );
    this.test.assertSelectorHasText( subtitleSelector, expectedSubtitle,
        'History subtitle has "' + expectedSubtitle + '": ' + this.fetchText( subtitleSelector ).trim() );

    this.test.comment( "tags and annotation icons should be available" );
    this.test.assertExists( tagIconSelector,  'Tag icon button found' );
    this.test.assertExists( annoIconSelector, 'Annotation icon button found' );

    this.test.comment( "A message about the current history being empty should NOT be displayed" );
    this.test.assertExists( emptyMsgSelector, emptyMsgSelector + ' exists' );
    this.test.assertNotVisible( emptyMsgSelector, 'Empty history message is NOT visible' );
});

// ------------------------------------------------------------------- tags
// keeping this light here - better for it's own test file
//TODO: check tooltips
spaceghost.withHistoryPanel( function openTags(){
    this.test.comment( 'tag area should open when the history panel tag icon is clicked' );

    this.click( tagIconSelector );
    this.wait( 1000, function(){
        this.test.assertVisible( tagAreaSelector, 'Tag area is now displayed' );
    });
});
spaceghost.withHistoryPanel( function closeAnnotation(){
    this.test.comment( 'annotation area should close when the history panel tag icon is clicked again' );

    this.click( tagIconSelector );
    this.wait( 1000, function(){
        this.test.assertNotVisible( tagAreaSelector, 'Tag area is now hidden' );
    });
});

// ------------------------------------------------------------------- annotation
// keeping this light here - better for it's own test file
//TODO: check tooltips
spaceghost.withHistoryPanel( function openAnnotation(){
    this.test.comment( 'annotation area should open when the history panel annotation icon is clicked' );

    this.click( annoIconSelector );
    this.wait( 1000, function(){
        this.test.assertVisible( annoAreaSelector, 'Annotation area is now displayed' );
    });
});
spaceghost.withHistoryPanel( function closeAnnotation(){
    this.test.comment( 'annotation area should close when the history panel tag icon is clicked again' );

    this.click( annoIconSelector );
    this.wait( 1000, function(){
        this.test.assertNotVisible( annoAreaSelector, 'Annotation area is now hidden' );
    });
});

// ------------------------------------------------------------------- refresh button
spaceghost.then( function refreshButton(){
    this.test.comment( 'History panel should refresh when the history refresh icon is clicked' );

    this.test.assertExists(  refreshButtonSelector, "Found refresh button" );
    this.test.assertVisible( refreshButtonSelector, "Refresh button is visible" );
    this.test.assertVisible( refreshButtonSelector + ' ' + refreshButtonIconSelector, "Refresh icon is visible" );
    this.test.assert( this.getElementAttribute( refreshButtonSelector, 'href' ) === refreshButtonHref,
        "Refresh button has href: " + refreshButtonHref );

    this.assertNavigationRequested( refreshButtonHref, "History refreshed when clicking refresh icon", function(){
        this.click( refreshButtonSelector );
    });
});

// ------------------------------------------------------------------- hdas can be expanded by clicking on the hda name
// broken in webkit w/ jq 1.7
spaceghost.historypanel.waitForHdas( function(){
    this.test.comment( 'HDAs can be expanded by clicking on the name' );
    var uploadedSelector = '#' + testUploadInfo.hdaElement.attributes.id;

    this.click( uploadedSelector + ' ' + this.historypanel.data.selectors.hda.title );
    this.wait( 1000, function(){
        this.test.assertVisible( uploadedSelector + ' ' + this.historypanel.data.selectors.hda.body,
            "Body for uploaded file is visible" );
    });
});

// ------------------------------------------------------------------- expanded hdas are still expanded after a refresh
spaceghost.then( function(){
    this.test.comment( 'Expanded hdas are still expanded after a refresh' );
    var uploadedSelector = '#' + testUploadInfo.hdaElement.attributes.id;

    this.click( refreshButtonSelector );
    this.historypanel.waitForHdas( function(){
        this.test.assertVisible( uploadedSelector + ' ' + this.historypanel.data.selectors.hda.body,
            "Body for uploaded file is visible" );
    });
    // this will break: webkit + jq 1.7
});

// ------------------------------------------------------------------- expanded hdas collapse by clicking name again
spaceghost.withHistoryPanel( function(){
    this.test.comment( 'Expanded hdas collapse by clicking name again' );
    var uploadedSelector = '#' + testUploadInfo.hdaElement.attributes.id;

    this.click( uploadedSelector + ' ' + this.historypanel.data.selectors.hda.title );
    this.wait( 500, function(){
        this.test.assertNotVisible( uploadedSelector + ' ' + this.historypanel.data.selectors.hda.body,
            "Body for uploaded file is not visible" );
    });
});

// ------------------------------------------------------------------- collapsed hdas still collapsed after a refresh
spaceghost.then( function(){
    this.test.comment( 'collapsed hdas still collapsed after a refresh' );
    var uploadedSelector = '#' + testUploadInfo.hdaElement.attributes.id;

    this.click( refreshButtonSelector );
    this.historypanel.waitForHdas( function(){
        this.test.assertNotVisible( uploadedSelector + ' ' + this.historypanel.data.selectors.hda.body,
            "Body for uploaded file is not visible" );
    });
});

// ===================================================================
spaceghost.run( function(){
    this.test.done();
});
