#!/usr/bin/python
#usage: python remove_redundant.py CP014449.16s.fasta test.fasta
import sys

def remove_redun(ori,fullseq,torm):
    for i in range(0,len(fullseq)-19):
        kmer = fullseq[i:i+20]
        if(ori.has_key(kmer)):
            num = ori[kmer]
            for j in range(num,num+20):
                torm[j]=j
            del ori[kmer]
    return ori,torm

def run_seq(ori,oriseq,name):
    #read reference file
    refread = open(sys.argv[2],'r')
    seqs=[]
    torm={}
    fullseq = ""
    for line in refread:
        if(line[:1]==">"):
            fullseq = ''.join(seqs)
            remove_redun(ori,fullseq,torm)
        else:
            seqs.append(line.strip())
    refread.close()
    #re assembly final seq
    print name
    for i in range(0,len(oriseq)):
        if not(torm.has_key(i)):
            sys.stdout.write(oriseq[i])
        else:
            sys.stdout.write('-')
    print ""

def main():
    #read original file
    ori = {}
    oriread = open(sys.argv[1],'r')
    seqs= []
    flag = 0
    name = ''
    for line in oriread:
        if(line[:1]==">" and flag == 0):
            flag = 1
            name = line.strip()
            continue
        elif (line[:1]==">" and flag == 1):
            fullseq = ''.join(seqs)
            for i in range(0,len(fullseq)-19):
                ids = fullseq[i:i+20]
                ori[ids]=i
            run_seq(ori,fullseq,name)
            ori = {}
            seqs=[]
            fullseq=''
            name = line.strip()
        else:
            seqs.append(line.strip())

    fullseq = ''.join(seqs)
    for i in range(0,len(fullseq)-19):
        ids = fullseq[i:i+20]
        ori[ids]=i
    oriread.close()
    
    run_seq(ori,fullseq,name)

if __name__ == '__main__':
    main()
