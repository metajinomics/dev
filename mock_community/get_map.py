#!/usr/bin/python

"""
usage: python get_map.py genbank_file > output
"""

import sys
from Bio import SeqIO


def main():
    gb_file = sys.argv[1]
#    gb_record = SeqIO.read(open(gb_file,'r'),'genbank')
    for gb_record in SeqIO.parse(gb_file,"genbank") :
        genome_name = gb_record.annotations["source"]
        for record in gb_record.features:
            if (record.type == "CDS"):
                for x in record.qualifiers:
                    if (x == "translation"):
                        ids = [">",record.qualifiers["locus_tag"][0]]
                        gene_name = "".join(ids)
                        print '\t'.join([genome_name,gene_name[1:]])


if __name__ == '__main__':
    main()
