#!/usr/bin/python
#find original seq using arg name
#python find_original_seq.py arg_list_three_org.uniq.txt usda.nu.fna 

import sys

def find_seq(locus, file):
    seq = ""
    flag = 0
    for line in open(file,'r'):
        if(line[:1] == ">"):
            spl = line[1:].strip().split(' ')
            if spl[0] == locus:
                flag = 1
                seq =  line.strip()+'\n'
                continue
        if(flag == 1):
            seq = seq+ line.strip()
            flag = 0
            
    return seq

def main():
    name = sys.argv[1]
    for x in open(name,'r'):
        gene = x.strip().split('\t')
        locus = gene[1]
        seq = find_seq(locus, sys.argv[2])
        fwrite = open(locus+'.fa','w')
        fwrite.write(seq)
        fwrite.close()

if __name__ == '__main__':
    main()

