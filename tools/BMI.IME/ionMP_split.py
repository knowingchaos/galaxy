import sys
import os

inname=sys.argv[1]
outname=sys.argv[2]
f=open(inname,'r')
g1=open(outname+'_1_temp.fastq','w')
g2=open(outname+'_2.fastq','w')
g3=open(outname+'_se.fastq','w')

switch_1 = 0
switch_2 = 0
write_buffer=[]
count = 0

for each in f:
    if (count == 0) & ('/1\n' in each) :
        switch_1 = 1
        
    if (count == 0) & ('/2\n' in each) :
        switch_2 = 1
    write_buffer.append(each)
    count += 1
    
    if count == 4:
        if switch_1 == 1:
            for each2 in write_buffer:
                g1.write(each2)
                
            write_buffer = []
            switch_1 = 0
        elif switch_2 == 1:
            for each2 in write_buffer:
                g2.write(each2)
            write_buffer = []
            switch_2 = 0
        else:
            for each2 in write_buffer:
                g3.write(each2)
                write_buffer = []
                
            
        write_buffer = []
        count = 0
            
    

f.close()
g1.close()
g2.close()
g3.close()        


f=open(outname+'_1_temp.fastq','r')
g=open(outname+'_1.fastq','w')

count = 0

for each in f:
    if count == 0:
        g.write(each)
    if count == 1:
        seq=each.strip('\n')
        new_seq=''
        for eachchar in seq:
            if eachchar == 'A':
                new_seq = 'T'+new_seq
            if eachchar == 'T':
                new_seq = 'A'+new_seq
            if eachchar == 'G':
                new_seq = 'C'+new_seq
            if eachchar == 'C':
                new_seq = 'G'+new_seq
        g.write(new_seq+'\n')
    if count == 2:
        g.write(each)
    if count == 3:
        qual = each.strip('\n\r')
        new_qual = ''
        for eachqual in qual:
            new_qual = eachqual+new_qual
        g.write(new_qual+'\n')
        count = -1
    count +=1

f.close()
g.close()

os.remove(outname+'_1_temp.fastq')
