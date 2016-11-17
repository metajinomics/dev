#this script generate splited gi file from blast output
#python blast_gi.py blast.output > gi.txt
import sys

cid = ""
i = 1
for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    gens = spl[0].split('|')
    gen = gens[len(gens)-1]
    ids = spl[1].split('|')[1]
    if (int(spl[8]) < int(spl[9])):
        print ids+'\t'+spl[8]+'-'+spl[9]+'\t'+'plus'
    else:
        print ids+'\t'+spl[9]+'-'+spl[8]+'\t'+'minus'
    cid = spl[0]
    i += 1

