#!/usr/bin/python 
"""
This script do ...
usage:
python find_center_seq.py list fasta
"""

import sys
import screed

def make_fasta_file(fasta, otu_name, li):
    otu_write = open(otu_name+".fa",'w')
    for one_list in li:
        if fasta.has_key(one_list):
            otu_write.write(">"+one_list+'\n'+fasta[one_list]+'\n')
    otu_write.close()

def main():
    #read fasta
    fasta = {}
    for record in screed.open(sys.argv[2]):
        fasta[record.name] = record.sequence

    #read list
    li = []
    otus = []
    seq_list = []
    for n,line in enumerate(open(sys.argv[1],'r')):    
        spl = line.strip().split('\t')
        if n == 0:
            otus = spl
        elif n == 1:
            seq_list = spl
        else:
            continue


    #find represent
    for i in range(2,len(otus)):
        li = seq_list[i].split(',')
        if len(li) > 2:
            #print otus[i], li
            make_fasta_file(fasta,otus[i],li)
    

if __name__ == '__main__':
    main()
