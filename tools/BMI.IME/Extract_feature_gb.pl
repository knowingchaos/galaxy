#usage：perl Extract_feature_gb.pl [infile] [outfile] [Feature];
#功能：从genbank文件中提取出序列的feature信息。genbank序列可以为多条信息

use strict;
#use warnings;
use Bio::SeqIO;

my $infile = $ARGV[0];
my $seqio_object = Bio::SeqIO->new(-file => "<$infile", -format => 'genbank');
my $featuretype = $ARGV[2];


open OUT, ">$ARGV[1]";	
print OUT "Accession\tDesription\tLength\tLocation\tSequence\tLocus_tag\tProduct\tGene\tNote\tDb_xref\tTranslation\n";   #打印xml表格的表头



while (my $sequence = $seqio_object->next_seq )
 {    
    my $seqname = $sequence->accession_number;         #   序列的名称 
    #my $seqs = $sequence->seq;                         #   序列字符串
    my $seq_length = $sequence->length;                #   序列长度
    my $descrip = $sequence->description;
       
       foreach my $feat_object ( grep { $_->primary_tag =~ /$featuretype/i } $sequence->get_SeqFeatures ) 
                     {
                        my ($gene_name) = $feat_object->get_tag_values('gene') if $feat_object->has_tag('gene');
                        my ($locus_tag) = $feat_object->get_tag_values('locus_tag') if $feat_object->has_tag('locus_tag');
                        my ($note) = $feat_object->get_tag_values('note') if $feat_object->has_tag('note');
                        #my ($codon_start) = $feat_object->get_tag_values('codon_start');
                        my ($product) = $feat_object->get_tag_values('product') if $feat_object->has_tag('product');
                        #my ($protein_id) = $feat_object->get_tag_values('protein_id');
                        my @db_xref = $feat_object->get_tag_values('db_xref') if $feat_object->has_tag('db_xref');
                        my $db_xref = join("|",@db_xref);
                        #my $strand = $feat_object->strand;
                        my $location;
                        my $sequence;
                        my $translation;
                        if ( $feat_object->location->isa('Bio::Location::SplitLocationI') )
                         {
                           foreach my $loc ( $feat_object->location->sub_Location )
                           {
                            $location = $location . "(" . $loc->start . ".." . $loc->end . ")";
                           }
                           
                           
                           $sequence = $feat_object->spliced_seq->seq; #出的结构正确
                           #$translation = $feat_object->spliced_seq->translate->seq;
                           ($translation) = $feat_object->get_tag_values('translation') if $feat_object->has_tag('translation');
                           #chop $translation;
                          }
                          
                        else
                          {
                           $location = "(" . $feat_object->location->start . ".." . $feat_object->location->end . ")";
                           $sequence = $feat_object->seq->seq;
                           #$translation = $feat_object->seq->translate->seq;
                           #chop $translation;
                           ($translation) = $feat_object->get_tag_values('translation') if $feat_object->has_tag('translation');
                          }
                       
                         print OUT "$seqname\t$descrip\t$seq_length\t$location\t$sequence\t$locus_tag\t$product\t$gene_name\t$note\t$db_xref\t$translation\n";
                     }
 }
