#功能：对已知顺序的contig用原始测序reads补gap
#usage:  perl  *.pl  $ctgs   $database.fa    $N(取末端长度)   $m（alignment阀值）  outfile（输出文件）

#将solexa部分数据(50~100倍覆盖于基因组)和454数据混合，效果会更好。

use strict;                                                                                         
use warnings;
use Bio::SeqIO;
use Bio::AlignIO;

my $inctg = Bio::SeqIO -> new ( -file  => "<$ARGV[0]" ,-format => 'fasta' );   #open ctg file
my $ctg_seq=0;
my $ctgID=0;
open(DATA,"<$ARGV[1]");
my @reads=grep(!/>/,<DATA>);    #将database中的序列数据读进内存
my $end=0;#初始化结头序列
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
    	###################### 处理第一条读数 #####################
      if($k==1){
         	    $end=substr($ctg_seq,length($ctg_seq)-30-$N,$N);
              $string=$end;
        	    
      last;}
      ###########################################  
      else{
      ##################### 分别对正反向取reads并左对齐  ########
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



      #####################   AlignIO读取consensus模块  ########
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
      ########################################################## 如果连接大于**则打印延长的部分，中断循环
         if(length($string)>=2000){
         	   open (OUT,">>$ARGV[4]");
             print OUT "\n$string\n";
             $end=substr($ctg_seq,length($ctg_seq)-30-$N,$N);
             $string=$end;
                                                     print"Extending is too long!\n";
       last;}
      ########################################################## 如果延长部分和原来的末端几乎相同，则打印延长部分，中断循环     
         if(length($consensus)<=2){
         	   open (OUT,">>$ARGV[4]");
             print OUT "\n$string\n";
             $end=substr($ctg_seq,length($ctg_seq)-30-$N,$N);
             $string=$end;
                                                     print"Extending is too short!\n";
 	     last;}
      ########################################################## 如果连通，则打印延长部分，并将下一条序列的名称去掉,中断循环      
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



      ################  更新末端小片段    ######################
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
