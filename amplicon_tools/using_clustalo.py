#!/usr/bin/python 
"""
This script do ...
usage:
python find_center_seq.py list fasta
"""

import sys
import screed

def make_fasta_file(file_name, otu_name, li):
    list_dict = {}
    for one_list in li:
        list_dict[li] = 0
    otu_write = open(otu_name+".fa",'w')
    for record in screed.open(file_name):
        if list_dict.has_kye(record.name):
            print ">"+record.name+"\n"+record.sequence
    otu_write.close()

def main():
    #read fasta
    

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

            print otus[i], li
            make_fasta_file(sys.argv[1],otus[i],li)
    

if __name__ == '__main__':
    main()
