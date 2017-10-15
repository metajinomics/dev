#!/usr/bin/python

"""
this script get organism info of CAZY
usage: python make_table.py cazy.fa
"""

import sys
import time
from Bio import SeqIO
from Bio import Entrez


def get_organism(genbank_id):
    organism = []
    Entrez.email = "genase23@gmail.com"
    handle = Entrez.efetch(db="protein",
                       id=genbank_id,
                       rettype="gb",
                       retmode="text")
    whole_sequence = SeqIO.parse(handle, "genbank")  
    for gb_record in whole_sequence:
        organism = gb_record.annotations['taxonomy']
    return organism
    
def main():
    #read 
    file_name = sys.argv[1]
    for line in open(file_name,'r'):
        if line[:1] == ">":
            genbank_id = line[1:].strip().split('|')[0]
            organism = get_organism(genbank_id)
            print genbank_id+'\t'+'\t'.join(organism)


if __name__ == '__main__':
    main()
