#!/usr/bin/python

"""
usage: python get_map.py genbank_file > output
"""

import sys
from Bio import SeqIO


def main():
    gb_file = sys.argv[1]

    for gb_record in SeqIO.parse(gb_file,"genbank") :
        genome_name = gb_record.annotations["source"]
        for record in gb_record.features:
            if (record.type == "CDS"):
                for x in record.qualifiers:
                    if (x == "translation"):
                        if record.qualifiers.has_key("locus_tag"):
                            gene_name = record.qualifiers["locus_tag"][0]
                        elif record.qualifiers.has_key("db_xref"):
                            gene_name = record.qualifiers["db_xref"][0]
                        else:
                            continue
                        print '\t'.join([genome_name,gene_name])


if __name__ == '__main__':
    main()
