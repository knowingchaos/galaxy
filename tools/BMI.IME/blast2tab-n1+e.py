# -*- coding: cp936 -*-
# 用途：将标准的blast结果转变为tab形式，并只输出前n条结果的第1段
# 语法：python command.py inputfile.blast outfile n


import re
import sys

qrymatch=re.compile(r'^Query=[\s\S]+?letters\)')                  # 提取Query= 直到letters)
qidmatch=re.compile(r'^Query=[\s\S]+\(')
qlenmatch=re.compile(r'\(.+letters\)')
longmatch=re.compile(r'[\d\,]+\,?\d*')
titmatch=re.compile(r'.{65,72}[\.\d]{1,8}\ {3}[e\d\.\s\-]+?\n')   # 提取前面带e值的行
intmatch=re.compile(r'\d+')
sbjmatch=re.compile(r'\n>')
sbjidmatch=re.compile(r'[\s\S]+?Length =.+\d+')
sbjlenmatch=re.compile(r'Length =.+?\d+')
segmatch=re.compile(r'Score =')
segscomatch=re.compile(r'\d+\.?\d*.+bits')
scomatch=re.compile(r'\d+\.?\d*')
#expmatch=re.compile(r'Expect .+= [e\d\.\s\-]+')               #提取e值
expmatch=re.compile(r'Expect.+= [e\d\.\s\-]+')               #提取e值
segidematch=re.compile(r'Identities =.+?\)')
segposmatch=re.compile(r'Positives =.+?\)')
divmatch=re.compile(r'\d+\/\d+')
permatch=re.compile(r'\(\d+%\)')
qrystamatch=re.compile(r'Query:.+?\d+')
qryendmatch=re.compile(r'Query:.+\d+')
sbjstamatch=re.compile(r'Sbjct:.+?\d+')
sbjendmatch=re.compile(r'Sbjct:.+\d+')

result=[]
result.append('Query ID'+'\t'+'Query len'+'\t'+'Subject ID'+'\t'+'Subject len'+'\t'+'seg id'\
              +'\t'+'seg score'+'\t'+'E-value'+'\t'+'Iden 1'+'\t'+'Iden 2'+'\t'+'Iden percent'+'\t'+'Positive 1'\
              +'\t'+'Positive 2'+'\t'+'Positive percent'+'\t'+'Query start'+'\t'+'Query end'\
              +'\t'+'Sbjct start'+'\t'+'Sbjct end'+'\n')
string=''
blastfile=sys.argv[1]
outf=sys.argv[2]
#blastfile='d:/temp/1.megablast'
n=int(sys.argv[3])
#n=3
rf=open(blastfile,'r')
for i in range(1000):
    temp=rf.next()
    if 'Query=' in temp:
        string=temp
        break
for each in rf:
    if 'Query=' in each or 'Matrix:' in each:
        if 'No hits found' in string:
            string=each
            continue
        if qrymatch.search(string)!=None:
            qry=qrymatch.search(string).group()
        else:
#            print string[:100]
            string=each
            continue
#        titles=titmatch.findall(string)
#        evalues=[]                            #存放e值
#        for t in titles:
#            e=t.strip().split()[-1]
#            if e[0]=='e':
#                e='1'+e
#            evalues.append(float(e))
#        enum=len(evalues)                     #存放e值的数量
        
        qid=qidmatch.search(qry).group()[6:-1].strip().replace('\n','').replace('  ','')
        qlen=longmatch.search(qlenmatch.search(qry).group()).group().replace(',','')
        subjects=sbjmatch.split(string)
        k=1
        for sbj in subjects[1:]:
            if sbjidmatch.search(sbj)==None:
                sbjidlen='#'
            else:
                sbjidlen=sbjidmatch.search(sbj).group()
            sbjid=sbjidlen.split('Length =')[0].strip().replace('\n','').replace('  ','')
            if sbjlenmatch.search(sbjidlen)==None:
                sbjlen=='#'
            else:
                if longmatch.search(sbjlenmatch.search(sbjidlen).group())==None:
                    sbjlen=='#'
                else:
                    sbjlen=longmatch.search(sbjlenmatch.search(sbjidlen).group()).group().replace(',','')
            segments=segmatch.split(sbj)
            j=1
            for seg in segments[1:2]:
                if segscomatch.search(seg)==None:
                    segsco='#'
                else:
                    segsco=segscomatch.search(seg).group()
                if scomatch.search(segsco)==None:
                    score='#'
                else:
                    score=scomatch.search(segsco).group()
                if expmatch.search(seg)==None:
                    exp='#'
                else:
                    exp=expmatch.search(seg).group().split('=')[1].strip()
                    if exp[0]=='e':
                        exp='1'+exp
                if segidematch.search(seg)==None:
                    iden='#'
                else:
                    iden=segidematch.search(seg).group()
                if divmatch.search(iden)==None:
                    iden1='#'
                    iden2='#'                
                else:
                    iden1=divmatch.search(iden).group().split('/')[0]
                    iden2=divmatch.search(iden).group().split('/')[1]
                if permatch.search(iden)==None:
                    idenper='#'
                else:
                    idenper=permatch.search(iden).group()[1:-1]
                if segposmatch.search(seg)!=None:
                    posi=segposmatch.search(seg).group()
                    if segposmatch.search(seg)==None:
                        posi1='#';posi2='#';posiper='#'
                    else:
                        posi1=divmatch.search(posi).group().split('/')[0]
                        posi2=divmatch.search(posi).group().split('/')[1]
                        posiper=permatch.search(posi).group()[1:-1] 
                else:
                    posi1='#';posi2='#';posiper='#'
                if qrystamatch.search(seg)==None:
                    qrysta='#'
                else:
                    qrysta=intmatch.search(qrystamatch.search(seg).group()).group()
                if qryendmatch.findall(seg)==None:
                    qryend='#'
                else:
                    qryend=intmatch.findall(qryendmatch.findall(seg)[-1])[-1]
                if sbjstamatch.search(seg)==None:
                    sbjsta='#'
                else:
                    sbjsta=intmatch.search(sbjstamatch.search(seg).group()).group()
                if sbjendmatch.findall(seg)==None:
                    sbjend='#'
                else:
                    sbjend=intmatch.findall(sbjendmatch.findall(seg)[-1])[-1]
#                if enum>=k:
#                    ev=evalues[k-1]
#                else:
#                    ev='#'
                result.append(qid+'\t'+qlen+'\t'+sbjid+'\t'+sbjlen+'\t'+str(j)+'\t'+score+'\t'+exp\
                              +'\t'+iden1+'\t'+iden2+'\t'+idenper+'\t'+posi1+'\t'+posi2+'\t'+posiper\
                              +'\t'+qrysta+'\t'+qryend+'\t'+sbjsta+'\t'+sbjend+'\n')                
                j=j+1
            if k>=n:
                    break
            k=k+1
        string=each
    else:
        string=string+each
rf.close()

wf=open(outf,'w')
for e in result:
    wf.write(e)
wf.close()
