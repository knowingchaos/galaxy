import sys

inname=sys.argv[1]
outname=sys.argv[2]

f=open(inname,'r')
g=open(outname,'w')

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
        for eachqual2 in qual:
            new_qual = eachqual2+new_qual
        g.write(new_qual+'\n')
        count = -1
    count +=1

f.close()
g.close()
            
