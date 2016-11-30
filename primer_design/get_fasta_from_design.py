#!/usr/bin/python

# this script print primers in fasta format from output file of PrimerDesign
# usage: python get_fasta_from_design.py output.design > output.fasta
# make truseq form of primer???? -> need to check
 
import sys
import reverse_complement
tru = 1

def main():
    num = 0
    file = sys.argv[1]
    #set = 0
    for line in open(file,'r'):
        genename = file.split('.')[0]
        if line[:13] == "Primer Pair: " :
            #set += 1
            prim = {}
            num += 1
            spl = line.strip().split("revOligo")
            for i in range(0,len(spl)):
                oli =  spl[i].split("seq=")
                snum = 0
                for j in range(1,len(oli)):
                    snum += 1
                    oneoli = oli[j].split("}")
                    if( i == 0):
                        print ">F:"+file+"_"+str(num)+"_"+str(snum)
                        print oneoli[0]
                    else:
                        print ">R:"+file+"_"+str(num)+"_"+str(snum)
                        print oneoli[0]


if __name__ == '__main__':
    main()
