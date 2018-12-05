#!/usr/bin/python 
"""
This script do ...
usage:
python find_center_seq.py distance_matrix.txt
"""

import sys

def get_represent_seq(file_name, name, li, one_otu):
    num = []
    for x in li:
        num.append(name[x])
    
    #read dist table
    read_name = open(file_name,'r')
    lines = read_name.readlines()
    diagonal_dist = {}
    for n,x in enumerate(li):
        temp_num = []
        for y in num:
            if y < name[x]:
                temp_num.append(y)
        temp_dist = []
        spl = lines[name[x]+1].strip().split('\t')

        value = spl[1:len(spl)]
        fvalue = []
        for x in value:
            fvalue.append(float(x))

        for one_temp_num in temp_num:
            temp_dist.append(fvalue[one_temp_num])

        diagonal_dist[n] = temp_dist
        last_num = n
    read_name.close()

    #make full table
    full_dist ={}
    for n in range(0,last_num+1):
        full_dist[n] = diagonal_dist[n]
        for i in range(n,last_num+1):
            if n ==  i:
                full_dist[n].append(1)
            else:
                full_dist[n].append(diagonal_dist[i][n])

    #calculate smallest
    smallest = 1000000000
    smallest_id = 0
    for item in full_dist.items():

        if sum(item[1]) < smallest:
            smallest = sum(item[1])
            smallest_id = item[0]


    print one_otu, li[smallest_id]


def main():
    #read name of sequence from dist table

    name = {}
    file_name = sys.argv[1]
    read_name = open(file_name,'r')
    for n,line in enumerate(read_name):
        if n == 0:
            continue
        spl = line.strip().split('\t')
        name[spl[0]] = n-1
    read_name.close()

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


    #find represent
    for i in range(2,len(otus)):
        li = seq_list[i].split(',')
        get_represent_seq(file_name, name, li, otus[i])

    

if __name__ == '__main__':
    main()
