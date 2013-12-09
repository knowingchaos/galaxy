#usage：perl Extract_inform_gb.pl [infile] [outfile]
#功能：从genbank文件中提取出序列的通用信息，如作者，时间，国家，来源等。genbank序列可以为多条信息

#!perl
use strict;
use warnings;
use Bio::SeqIO;


my $infile = $ARGV[0];
my $seqio_object = Bio::SeqIO->new(-file => "<$infile", -format => 'genbank');

open OUT, ">$ARGV[1]";	
print OUT "Accession\tLength\tDescription\tClassification\tReference\tOrganism\tCountry\tCollection_date\tHost\n";   #打印xml表格的表头



while (my $sequence = $seqio_object->next_seq )
{    
    my $accession = $sequence->accession_number;        
    #my $seqs = $sequence->seq;  
    #my ($date) =  $sequence->get_dates;    
    my $description = $sequence->description;
    my $leng = $sequence->length;  
    my $species = $sequence->species->common_name;
    my @classification = $sequence->species->classification;
       @classification = reverse (@classification);
       my $classification = join ( "; ", @classification );



    ####################### Reference ############################
    my $reference = "";
    my $anno_collection = $sequence->annotation;
    my @key = $anno_collection->get_all_annotation_keys;
    foreach my $key ( @key )
      {
         my @annotations = $anno_collection->get_Annotations($key);
         foreach my $value ( @annotations )
         {
          my $tagname = $value->tagname;
          if( $tagname eq "reference" )
           {
           #my $authors = $value->authors;
           my $title = $value->title;
           my $location = $value->location;
           if(!($title=~/Direct Submission/))
              {$reference.= $title."|".$location."#";}
           }
         }
       }
    ############################################################# 
      
       
    ##################### Source ################################# 
    my $organism = "";
    my $country = "";
    my $collection_date = "";
    my $host = "";
    foreach my $feat_object ( grep { $_->primary_tag eq "source" } $sequence->get_SeqFeatures ) 
      {
      ($organism) = $feat_object->get_tag_values("organism") if $feat_object->has_tag('organism');
      ($country) = $feat_object->get_tag_values('country') if $feat_object->has_tag('country');   
     	($collection_date) = $feat_object->get_tag_values('collection_date') if $feat_object->has_tag('collection_date');   
     	($host) = $feat_object->get_tag_values('host') if $feat_object->has_tag('host');   
     	($host) = $feat_object->get_tag_values('lab_host') if $feat_object->has_tag('lab_host');   
      }
    ##############################################################


print OUT "$accession\t$leng\t$description\t$classification\t$reference\t$organism\t$country\t$collection_date\t$host\n";
      
}     