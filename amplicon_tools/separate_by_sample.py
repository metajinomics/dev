#!/usr/bin/python
# this script separate fastq file into samples
#usage: python separate_by_sample.py mapping_file barcode_file fastq R1/R2 directory 
import sys
from string import maketrans
import os

def add_seq(seq,ids,result):
    if( ids.has_key(seq[0].split(' ')[0])):
        samid = ids[seq[0].split(' ')[0]]
        if (result.has_key(samid)):
            temp = result[samid]
            temp.append('\n'.join(seq))
            result[samid]=temp
        else:
            result[samid]= ['\n'.join(seq)]

def get_rc(seq):
    seq = seq.upper()
    trans = maketrans("AGCT","TCGA")
    seq = seq.translate(trans,'xm')
    seq = seq[::-1]
    return seq

def check_barcode(seq,dict,result):
    barcode = seq[1]
    if( dict.has_key(barcode)):
        samid = dict[barcode]
        if (result.has_key(samid)):
            print "duplicated id"
        else:
            result[seq[0].split(' ')[0]]=dict[barcode]

def main():
    #step1: read mapping file
    dict = {}
    inforead = open(sys.argv[1],'r')
    for line in inforead:
        if (line[:1] == "#"):
            continue
        else:
            spl = line.strip().split('\t')
            dict[spl[1]] = spl[0]
            rev = get_rc(spl[1])
            dict[rev] = spl[0]
    inforead.close()

    #step2: read barcode file
    barread = open(sys.argv[2],'r')
    seq  = [] 
    ids = {}
    for n,line in enumerate(barread):
        if( n % 4 == 3):
            seq.append(line.strip())
            check_barcode(seq,dict,ids)
            seq = []
        else:
            seq.append(line.strip())
    barread.close()
    
    #step3: read raw-read file
    seqread = open(sys.argv[3],'r')
    seq = []
    result = {}
    for n,line in enumerate(seqread):
        if (n % 4 == 3):
            seq.append(line.strip())
            add_seq(seq,ids,result)
            seq = []
        else:
            seq.append(line.strip())
    seqread.close()

    #step4: write files
    di = sys.argv[4]
    loc = sys.argv[5]
    os.mkdir(loc)
    for item in result.items():
        fwrite = open("./"+loc+"/"+item[0]+"."+di+".fastq",'w')
        for x in  item[1]:
            fwrite.write(x+'\n')
        fwrite.close()

if __name__ == '__main__':
    main()
