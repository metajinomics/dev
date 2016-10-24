
#find original seq using arg name
#python find_original_seq.py /Users/jinchoi/Box\ Sync/2016/9September/mock/three_genome/arg_list_three_org.uniq.txt /Users/jinchoi/Box\ Sync/2016/9September/mock/three_genome/usda_arg.fa > tet38.fa

import sys

def find_seq(locus, file):
    seq = ""
    flag = 0
    for line in open(file,'r'):
        if(line[:1] == ">"):
            spl = line[1:].strip().split(' ')
            if spl[0] == locus:
                flag = 1
                print line.strip()
                continue
        if(flag == 1):
            print line.strip()
            flag = 0
            
    return seq

def find_locus(name, file):
    locus = ""
    for line in open(file,'r'):
        spl = line.strip().split('\t')
        if(spl[2] == name):
            locus = spl[1]
    return locus

def main():
    name = sys.argv[1]
    locus = find_locus(name, sys.argv[2])
    seq = find_seq(locus, sys.argv[3])

if __name__ == '__main__':
    main()

