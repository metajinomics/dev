#this script match map file and blast result
#output: organism, locus, ARG name
#python match_map_blast.py mapfile blastfile > output.txt

import sys
import utils

map = utils.read_map(sys.argv[1])

for line in open(sys.argv[2],'r'):
    spl = line.strip().split('\t')
    arg = spl[1].split('|')
    ar = arg[len(arg)-1]
    if(map.has_key(spl[0])):
        result = [ map[spl[0]], spl[0], ar]
        print '\t'.join(result)
