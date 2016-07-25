#!/usr/bin/python
# find primer interaction
# python primer_dimer.py primer.fa

import sys

def fl(seq):
    return seq[::-1]

def get_kmer(seq):
    kmer = []
    for i in range(5,len(seq)):
        for j in range(0,len(seq)-i):
            kmer.append( seq[j:i+j])                       
    return kmer

def cal_tm(one,two):
    tm = 0
    #print one
    #print two
    a = 0
    g = 0
    c = 0
    t = 0
    for i in range(0,len(one)):
        if(one[i]=="A" and two[i]=="T"):
            a += 1
        elif (one[i]=="T" and two[i]=="A"):
            t += 1
        elif (one[i]=="G" and two[i]=="C"):
            g += 1
        elif(one[i]=="C" and two[i]=="G"):
            c += 1
    #print a,g,c,t
    add = a+g+c+t
    if(add <14):
        tm = (a+t)*2 + (g+c)*4
    else:
        if(add == 0):
            tm = 0
        else:
            tm = 64.9 + 41*(g+c - 16.4)/(a+t+g+c)
    return tm
    
def compare(y,mer,cont,co):
    tm = []
    for i in range(0,len(y)-len(mer)+1):
        a = y[i:len(mer)+i]
        b = mer
        temp = cal_tm(a,b)
        cont += 1
        if(temp > 40):
            co += 1
            print y
            print temp
            tm.append(temp)
    return cont,co

#read primers
primer = []
for line in open(sys.argv[1],'r'):
    if(line[:1]=='>'):
        continue
    primer.append(line.strip().upper())

#print primer
cont = 0
co = 0
for x in primer:
    se = fl(x)
    #print x
    #print se
    kmer = get_kmer(se)
    for y in primer:
        for mer in kmer:
            #print y
            #print mer
            cont,co = compare(y,mer,cont,co)
print co
print cont
