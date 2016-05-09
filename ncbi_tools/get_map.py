#This script generate map: genome, gene_name(locus)
#usage: for x in *.gbk;do python get_map.py $x;done > output 
from Bio import SeqIO
import sys
gb_file = sys.argv[1]
gb_record = SeqIO.read(open(gb_file,'r'),'genbank')

for record in gb_record.features:
    if (record.type == "CDS"):
        for x in record.qualifiers:
            if (x == "translation"):
                ids = [">",record.qualifiers["locus_tag"][0]]
                gene_name = "".join(ids)
                print '\t'.join([gb_file,gene_name])

