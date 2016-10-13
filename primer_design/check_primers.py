#!/usr/bin/python
#this script check quality of primer by using primer3
#this script requires primer3 program installed
#usage: python check_primers.py oligotn_path ntthal_path primer_file 
#usage: python check_primers.py /Users/jinchoi/programs/primer3-2.3.7/src/oligotm /Users/jinchoi/programs/primer3-2.3.7/src/ntthal /Users/jinchoi/Box\ Sync/2016/10October/mock_primer_design/tet38.primer.txt 

import sys
import utils
import os

def check_hair(primer,ntthal, maxHair):
    spl = ntthal.split('/')
    config = '/'.join(spl[0:len(spl)-1])
    command = ntthal + " -dv 1.5 -n 0.6 -a HAIRPIN -r -path "+config+"/primer3_config/ -s1 "+ primer
    temp = os.popen(command).read().strip()
    if (float(temp) > maxHair):
        print primer, temp, "Hairpin"

def check_mt(primer,oligotm,minTm,maxTm):
    command = oligotm + " -sc 1 -tp 1 -dv 1.5 -n 0.6 " + primer
    temp = os.popen(command).read().strip()
    if (float(temp) > maxTm or float(temp) < minTm):
        print primer, temp, "Melting Temperature"

def main():
    oligotm = sys.argv[1]
    ntthal = sys.argv[2]
    minTm = 55
    maxTm = 100
    maxHair = 24
    #read primer
    file = sys.argv[3]
    fpri,rpri = utils.read_trad_primer(file)
    #print fpri
    #print rpri
    for f in fpri:
        check_mt(f,oligotm, minTm, maxTm)
        check_hair(f,ntthal,maxHair)
    for r in rpri:
        check_mt(r,oligotm, minTm, maxTm)
        check_hair(r,ntthal,maxHair)

if __name__ == '__main__':
    main()
