#!/usr/bin/python 
"""
This script do ...
usage:
python find_center_seq.py distance_matrix.txt
"""

import sys

def get_represent_seq(dist,name, li):
    num = []
    for x in li:
        num.append(name[x])

    diagonal_dist = {}
    for n,x in enumerate(li):
        temp_num = []
        for y in num:
            if y < name[x]:
                temp_num.append(y)
        temp_dist = []
        for z in temp_num:
            temp_dist.append(dist[x][z])

        diagonal_dist[n] = temp_dist
        last_num = n


    full_dist ={}
    for n in range(0,last_num+1):
        full_dist[n] = diagonal_dist[n]
        for i in range(n,last_num+1):
            if n ==  i:
                full_dist[n].append(1)
            else:
                full_dist[n].append(diagonal_dist[i][n])


    smallest = 1000000000
    smallest_id = 0
    for item in full_dist.items():

        if sum(item[1]) < smallest:
            smallest = sum(item[1])
            smallest_id = item[0]


    print li[smallest_id]


def main():
    #read dist table
    #dist = {}
    name = {}
    for n,line in enumerate(open(sys.argv[1],'r')):
        if n == 0:
            print line,
            continue
        spl = line.strip().split('\t')
        #value = spl[1:len(spl)]
        #fvalue = []
        #for x in value:
        #    fvalue.append(float(x))
        name[spl[0]] = n-1
        if n % 10000 == 0:
            print n
        #dist[spl[0]] = fvalue

    #read list
    li = []
    otus = []
    seq_list = []
    for n,line in enumerate(open(sys.argv[2],'r')):    
        spl = line.strip().split('\t')
        if n == 0:
            otus = spl
        elif n == 1:
            seq_list = spl
        else:
            continue

    print otus[0], otus[1], otus[2]
    spl = seq_list[2].split(',')
    print len(spl)
    print spl

    #get_represent_seq(dist,name, li)

    

if __name__ == '__main__':
    main()
