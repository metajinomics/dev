#!/usr/bin/python
# python get_pssm.py aligned.fa > pssm

import sys
def get_pssm(seqs):
    pssm = []
    ratio = []
    
    return pssm

def main():
    fread = open(sys.argv[1],'r')
    lines = fread.readlines()
    flag = 0
    seqs = []
    tempseq = []
    #read seed sequences
    for n,line in enumerate(lines):
        if(line[:1]==">" and flag == 0):
            flag = 1
            continue
        elif (line[:1]==">" and flag == 1):
            seqs.append(''.join(tempseq))
            tempseq = []
        else:
            tempseq.append(line.strip())
    #last line
        if(n == len(lines)-1):
            #do lastline
            seqs.append(''.join(tempseq))
            
    fread.close()

    for x in seqs:
        print len(x)
    #make pssm
    pssm = get_pssm(seqs)

if __name__ == '__main__':
    main()
