#!c:\usr\bin\perl-w

#usage: reverse_complement.pl inname outname
#���ļ��е�����contig���з��򻥲�
use strict;
use Bio::SeqIO;


my $infile = $ARGV[0];
my $putfile = $ARGV[1];

my $inseq = Bio::SeqIO -> new ( -file  => "<$infile" ,-format => 'fasta' );   #open the file
open (OUTHANDLE, ">$putfile");


my $k = 0;
while (my $seq = $inseq -> next_seq) {
	#����������  
	$k++; 
	my $seqstr = $seq -> seq();              #��ȡ���У���bioinformatics������577ҳ
	my $myID = $seq->display_id();
	my $long = length($seqstr);
	my $revcom = reverse $seqstr;
	$revcom =~ tr/ACGTacgt/TGCAtgca/;
	
	print OUTHANDLE ">"."$myID\n";
	print OUTHANDLE "$revcom\n";
			


	}

close OUTHANDLE;

exit;
		
		