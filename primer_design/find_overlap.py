#find overlap
#python find_overlap.py list usda.nu.fna *.trad.txt

import sys
import utils

def find_presence(gene,filelist,algene):
    fpri = []
    rpri = []
    for x in filelist:
        if(gene in x):
            fpri,rpri =  utils.read_trad_primer(x)
    fon = []
    for i in range(0,len(fpri)):
        if(utils.if_amplified(fpri[i],rpri[i],algene[gene])):
            fon.append([fpri[i],rpri[i]])
    return fon

def show_overlap(fon1,fon2):
    for x in fon1:
        for y in fon2:
            if(x[0] == y[0]):
                print x

def find_overlap(it,algene):
    gene1 = it[1]
    gene2 = it[2]

    filelist = sys.argv[3:]
    fon1 = find_presence(gene1,filelist,algene)
    fon2 = find_presence(gene2,filelist,algene)
    show_overlap(fon1,fon2)

def read_list(file):
    li = []
    for line in open(file,'r'):
        spl = line.strip().split('\t')
        if(len(spl)==3):
            li.append([spl[0],spl[1].split(':')[0],spl[2].split(':')[0]])
    return li

def main():
    #read list
    li = read_list(sys.argv[1])
    #read fasta
    algene = utils.read_fasta_usda(sys.argv[2])
    
    #find overlap
    for it in li:
        find_overlap(it,algene)

if __name__ == '__main__':
    main()
