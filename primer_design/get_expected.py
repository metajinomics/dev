#!/usr/bin/python 
"""
This script get expected product using design output
usage:
python get_expected.py design.out fasta.fa > expected.fa
"""

import sys
import screed
from string import maketrans
import re

def get_product(fpri,rpri,se,name):
    product = ''
    psize = 0
    pfpri = ''
    prpri = ''
    for x in fpri.items():
        ma = [m.start() for m in re.finditer(x[0], se)]
        if len(ma) > 0:
            for st in ma:
                tempseq = se[st:st+400]
                for y in rpri.items():
                    rma = [m.start() for m in re.finditer(y[0],tempseq)]
                    if len(rma) > 0 :
                        for rst in rma:
                            product = tempseq[:rst+len(y[0])]
                            psize = len(product)
                            pfpri = x[0]
                            prpri = y[0]
                            print ">%s %s(%s) %s %s(%s) %s %s\n%s" %(name, pfpri,fpri[pfpri],st, get_rc(prpri),rpri[prpri],st+rst+len(y[0]),len(product), product)
    return 0


def print_pcr_product(prim, seq_list, fasta):
    fpri = {}
    rpri = {}
    for item in prim.items():
        fpri[item[1]]= item[0]
        rpri[get_rc(item[1])] = item[0]

    for one_name in seq_list:
        name = one_name
        se = fasta[one_name]

        get_product(fpri,rpri,se,name)


def get_rc(seq):
    seq = seq.upper()
    trans = maketrans("AGCT","TCGA")
    seq = seq.translate(trans,'xm')
    seq = seq[::-1]
    return seq

def main():
    #read fasta
    fasta = {}
    for item in screed.open(sys.argv[2]):
        fasta[item.name] = item.sequence
    
    #read design out file
    num = 0
    file = sys.argv[1]
    seq_list = []
    prim = {}
    flag = 0
    for line in open(file,'r'):
        if line[:13] == "Primer Pair: " :
            flag = 1
            prim = {}
            num += 1
            seq_list = []
            spl = line.strip().split("revOligo")
            for i in range(0,len(spl)):
                oli =  spl[i].split("seq=")
                snum = 0
                for j in range(1,len(oli)):
                    snum += 1
                    oneoli = oli[j].split("}")
                    cnu = str(num)
                    pnu = str(snum)
                    if len(cnu) == 1:
                        cnu = "00"+cnu
                    elif len(cnu) == 2:
                        cnu = "0" + cnu

                    if len(pnu) == 1:
                        pnu = "0"+pnu

                    if( i == 0):
                        prim["F:"+file+".C"+cnu+"."+pnu+"F"]= oneoli[0]
                    else:
                        prim["R:"+file+".C"+cnu+"."+pnu+"R"]= oneoli[0]
        elif line[:10] == "----------":
            if flag == 1:
                print_pcr_product(prim, seq_list, fasta)
                prim = {}
            flag = 0
        elif line[:13] == "Sequences hit":
            continue
        else:
            seq_list.append(line.strip())
        


if __name__ == '__main__':
    main()
