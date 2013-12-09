#!c:\usr\bin\perl-w

#usage: reverse_complement.pl inname outname
#对文件中的所有contig进行反向互补
use strict;
use Bio::SeqIO;


my $infile = $ARGV[0];
my $putfile = $ARGV[1];

my $inseq = Bio::SeqIO -> new ( -file  => "<$infile" ,-format => 'fasta' );   #open the file
open (OUTHANDLE, ">$putfile");


my $k = 0;
while (my $seq = $inseq -> next_seq) {
	#逐条读序列  
	$k++; 
	my $seqstr = $seq -> seq();              #获取序列，见bioinformatics第三版577页
	my $myID = $seq->display_id();
	my $long = length($seqstr);
	my $revcom = reverse $seqstr;
	$revcom =~ tr/ACGTacgt/TGCAtgca/;
	
	print OUTHANDLE ">"."$myID\n";
	print OUTHANDLE "$revcom\n";
			


	}

close OUTHANDLE;

exit;
		
		