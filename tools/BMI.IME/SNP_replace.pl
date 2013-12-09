#作用，按照指定的snp_table_file将序列中的SNP替换过来
#snp_table_file可以从CLC的SNP——detection后生产的excel表中拷贝出来，格式为：
#Reference position   Allele variations
#1027	T	C              
#427	T	C              
#443	C	A              
#358	T	C              
#289	C	T              
#352	A	G              
#688	T	C              
#973	A	G              
#1135	T	C              
#970	C	T              

#用法：perl SNP_replace.pl    序列file    snp_table_file   outfile



#!/usr/bin/perl
use strict;                                                                                         
#use warnings;
use Bio::SeqIO;

my $inctg = Bio::SeqIO -> new ( -file  => "<$ARGV[0]" ,-format => 'fasta' );   #open ctg file
my $ctg_seq=0;
my $ctgID=0;

while (my $inctg = $inctg -> next_seq) 
{  
	 $ctg_seq = $inctg -> seq();$ctgID = $inctg ->display_id();

   open(FILE,"<$ARGV[1]");
   open(OUT,">$ARGV[2]");
   my $sta=0;
   my $end=0;
   my $position=0;
   while(<FILE>)
     {                chomp;
   		                my @data = split(/	/, $_);
   		                my $position=$data[0];
    	                my $raw=$data[1];
    	                my $now=$data[2];
    		              substr($ctg_seq, $position-1, 1, $now=$data[2]);
   		}
print OUT ">$ctgID\n$ctg_seq\n";

   	}

