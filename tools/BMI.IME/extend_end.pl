#���ܣ�����֪˳���contig��ԭʼ����reads��gap
#usage:  perl  *.pl  $ctgs   $database.fa    $N(ȡĩ�˳���)   $m��alignment��ֵ��  outfile������ļ���

#��solexa��������(50~100�������ڻ�����)��454���ݻ�ϣ�Ч������á�

use strict;                                                                                         
use warnings;
use Bio::SeqIO;
use Bio::AlignIO;

my $inctg = Bio::SeqIO -> new ( -file  => "<$ARGV[0]" ,-format => 'fasta' );   #open ctg file
my $ctg_seq=0;
my $ctgID=0;
open(DATA,"<$ARGV[1]");
my @reads=grep(!/>/,<DATA>);    #��database�е��������ݶ����ڴ�
my $end=0;#��ʼ����ͷ����
my $sta=0;
my $N=$ARGV[2];
my $i=0;
my $j=0;
my $k=0;
my $h=0;
my $string=0;
system("rm $ARGV[4]");

while (my $inctg = $inctg -> next_seq) 
{
	 $ctg_seq =uc($inctg -> seq());
	 
	 $ctgID = $inctg ->display_id();
   $sta = substr($ctg_seq,30,$N);  
   $k++;
         	                                             print "This is contig:$ctgID\n";
   while(1)
    { 
    	###################### �����һ������ #####################
      if($k==1){
         	    $end=substr($ctg_seq,length($ctg_seq)-30-$N,$N);
              $string=$end;
        	    
      last;}
      ###########################################  
      else{
      ##################### �ֱ��������ȡreads�������  ########
         open (OU,">$ARGV[4]temp.fa");
         my @hits= grep(/$end/,@reads);
         foreach(@hits){$j++;chomp;
         	 s/^.*$end/$end/;
         	 print OU ">$j\n", "$_\n";
         	}
         
         my $rend =reverse $end;;
         $rend =~ tr/ACGTacgt/TGCAtgca/;
         my @hits2=grep(/$rend/,@reads);
         foreach(@hits2){$j++;chomp;
         	 s/$rend.*/$rend/;
         	 $_ = reverse $_;
		       $_ =~ tr/ACGTacgt/TGCAtgca/;  
         	 print OU ">$j\n", "$_\n";
         	}
         	                                             print "Greped $j reads!\n";
         close OU;
         $j=0;
      ###########################################



      #####################   AlignIO��ȡconsensusģ��  ########
         my $consensus=0;
         my @temp2=0;
         my $str = Bio::AlignIO->new(-file => "$ARGV[4]temp.fa",-format => 'fasta');
         while(my $aln = $str->next_aln()){
         	$consensus=$aln->consensus_string($ARGV[3]);
         	                                             print "Consensus is:$consensus\n";
         	@temp2 = split(/\?/,$consensus);
         	$consensus=$temp2[0];	
         	}
         	                                             #print"Consensus is:$consensus\n";
      ##########################################################

         
         $consensus =~ s/^$end//;
         $string .= $consensus;
      ########################################################## ������Ӵ���**���ӡ�ӳ��Ĳ��֣��ж�ѭ��
         if(length($string)>=2000){
         	   open (OUT,">>$ARGV[4]");
             print OUT "\n$string\n";
             $end=substr($ctg_seq,length($ctg_seq)-30-$N,$N);
             $string=$end;
                                                     print"Extending is too long!\n";
       last;}
      ########################################################## ����ӳ����ֺ�ԭ����ĩ�˼�����ͬ�����ӡ�ӳ����֣��ж�ѭ��     
         if(length($consensus)<=2){
         	   open (OUT,">>$ARGV[4]");
             print OUT "\n$string\n";
             $end=substr($ctg_seq,length($ctg_seq)-30-$N,$N);
             $string=$end;
                                                     print"Extending is too short!\n";
 	     last;}
      ########################################################## �����ͨ�����ӡ�ӳ����֣�������һ�����е�����ȥ��,�ж�ѭ��      
         if($string =~ /$sta/){
         	   $string =~ s/$sta.*//;
             open (OUT,">>$ARGV[4]");
             print OUT "\n$string\n";
             $end=substr($ctg_seq,length($ctg_seq)-30-$N,$N);
             $string=$end;
             $i=1;
             $h++;
 	     last;}
       ##########################################################



      ################  ����ĩ��СƬ��    ######################
          $end = substr($string,length($string)-$N,$N);

                                                 # print"New string end is:$end\n";
       }
    }
          
      $ctg_seq=substr($ctg_seq,30,length($ctg_seq)-60-$N);

      ##########################################################
      if($i==0){
         open (OUT,">>$ARGV[4]");
         print OUT ">$ctgID\n","$ctg_seq\n";
        }
      else{
         open (OUT,">>$ARGV[4]");
         print OUT "$ctg_seq\n";
         $i=0;
                                                     print"$ctgID Connected!\n";
        }
      ##########################################################

}

print "There are $k contigs. $h contigs are connected!\n";
system("rm $ARGV[4]temp.fa");
