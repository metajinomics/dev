#!/usr/bin/python

import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

def get_16s(genbankname):
    genome=SeqIO.read(genbankname, 'genbank')

    n = 0
    l = []

    for record in list(SeqIO.parse(genbankname, 'genbank')):
        org = record.annotations["source"]
        for feat in genome.features:
            if feat.type == "rRNA":
                if '16S' in feat.qualifiers['product'][0]:#or '16S ribosomal' for strict match
                    start = feat.location.start.position
                    end = feat.location.end.position
                    pos = [start, end]
                    l.append(pos)
                    if n==0:
                        #print '>' + genbankname.split('.')[0] + ' ' + org + ' '+ '16S rRNA gene' + str(n)
                        print '>' + org + ' '+ '16S rRNA gene' + str(n) 
                        print feat.extract(genome.seq)
                    n = n + 1
    return n

def main():
    file = open(sys.argv[1],'r')
    for line in file:
        if(line.strip()==""):
            continue
        genbankname = line.strip()+".gbk"

        get_16s(genbankname)

if __name__ == '__main__':
    main()
