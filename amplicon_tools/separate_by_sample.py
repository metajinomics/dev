#!/usr/bin/python
# this script separate fastq file into samples
#usage: python separate_by_sample.py desciption fastaq 
import sys


def check_barcode(seq,dict,result):
    barcode = seq[1][-12:]
    if( dict.has_key(barcode)):
        samid = dict[barcode]
        if (result.has_key(samid)):
            temp = result[samid]
            temp.append('\n'.join(seq))
            result[samid]=temp
        else:
            result[samid]=['\n'.join(seq)]
def main():
    dict = {}
    inforead = open(sys.argv[1],'r')
    for line in inforead:
        if (line[:1] == "#"):
            continue
        else:
            spl = line.strip().split('\t')
            dict[spl[3]] = spl[0]

    seqread = open(sys.argv[2],'r')
    seq  = [] 
    result = {}
    for n,line in enumerate(seqread):
        if( n % 4 == 3):
            seq.append(line.strip())
            check_barcode(seq,dict,result)
            seq = []
        else:
            seq.append(line.strip())
    for item in result.items():
        fwrite = open(item[0]+".R1.fastq",'w')
        for x in  item[1]:
            fwrite.write(x+'\n')
        fwrite.close()

if __name__ == '__main__':
    main()
