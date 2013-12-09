#!c:\usr\bin\perl-w

#usage: rev_com_rev.pl inname outname
#���ܣ� ���������е�fa�ļ�ÿ�����з��򻥲���ͬʱ�����ʱ��ߵ��������е�˳��
use strict;
use Bio::SeqIO;


my $infile = $ARGV[0];
my $putfile = $ARGV[1];

my $inseq = Bio::SeqIO -> new ( -file  => "<$infile" ,-format => 'fasta' );   #open the file
open (OUTHANDLE, ">$putfile");


my $k=0;
my $i=0;
my @file=0;
while (my $seq = $inseq -> next_seq) {
	my $seqstr = $seq -> seq();
	my $myID = $seq->display_id();
	my $revcom = reverse $seqstr;
	$revcom =~ tr/ACGTacgt/TGCAtgca/;


	$file[$k]= ">".$myID.'*'.$revcom;
	$k++; 
	}
	
	
	
for($i=$k-1;$i>=0;$i--){
	my @file2=split(/\*/, $file[$i]);
	print OUTHANDLE "$file2[0]\n$file2[1]\n";
}
close OUTHANDLE;

		
		