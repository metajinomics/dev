#
#python blast_gi.py blast.output > gi.txt
import sys

for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    ids = spl[1].split('|')[1]
    if (int(spl[8]) < int(spl[9])):
        print ids+'\t'+spl[8]+'-'+spl[9]
