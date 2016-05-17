#!/bin/usr/python
#this script get protein sequence from genbank file
# usage: python fetch_protein.py genbankfile > output.fa

from Bio import SeqIO
import sys
gb_file = sys.argv[1]
gb_record = SeqIO.read(open(gb_file,'r'),'genbank')
#print "Name %s, %i features" % (gb_record.name, len(gb_record.features))
#gb_feature = gb_record.features[1]
#print gb_feature.extract(gb_record.seq).translate(table=11, cds=True)
#for seq_record in SeqIO.read(open(sys.argv[1],'r'),'genbank'):
#    print seq_record
#    for feat in seq_record.features:
#        if feat.type == "CDS":
#            print fet.type
#            print feat.translation
for record in gb_record.features:
    if (record.type == "CDS"):
        for x in record.qualifiers:
            if (x == "translation"):
                ids = [">",record.qualifiers["locus_tag"][0]]
                product = record.qualifiers["product"][0]
                print "".join(ids),product
                print record.qualifiers["translation"][0]
#        print record.extract(gb_record.seq).translate(table=11,cds=True)
