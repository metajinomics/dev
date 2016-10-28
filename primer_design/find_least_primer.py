
#usage: python find_least_primer.py arg_list_three_org.uniq.txt rawprimer/

import sys
from os import listdir
from os.path import isfile, join
import utils

def merge(shared_f_from_p1, shared_r_from_p1,shared_f_from_p2, shared_r_from_p2):
    shared_f = {}
    shared_r = {}
    if(len(shared_f_from_p1) > 0 and len(shared_f_from_p2)>0):
        for item in shared_f_from_p1.items():
            shared_f[item[0]] = item[1]
        for item in shared_f_from_p2.items():
            shared_f[item[0]] = item[1]

    for item in shared_r_from_p1.items():
        shared_r[item[0]] = item[1]
    for item in shared_r_from_p2.items():
        shared_r[item[0]] = item[1]

    return shared_f, shared_r

def find_share(fp,rp,seq1,seq2):
    shared_f_from_p1 = {}
    shared_r_from_p1 = {}
    testf = []
    testr = []

    for x in fp:
        temp = []
        p_in_seq = seq1.find(x)
        temp.append(p_in_seq)
        testf.append(temp)
    for x in rp:
        temp = []
        p_in_seq = seq1.find(x)
        temp.append(p_in_seq)
        testr.append(temp)

    i= 0
    for x in fp:
        p_in_seq = seq2.find(x)
        temp = testf[i]
        temp.append(p_in_seq)
        testf[i] = temp
        i += 1
    i=0
    for x in rp:
        p_in_seq = seq2.find(x)
        temp = testr[i]
        temp.append(p_in_seq)
        testr[i] = temp
        i += 1

    for i in range(0,len(testf)):
        if(testf[i][0] >0 and testf[i][1] > 0):
            shared_f_from_p1[fp[i]] = testf[i]


    for i in range(0,len(testr)):
        if(testr[i][0] == 1 and testr[i][1] == 1):
            shared_r_from_p1[rp[i]] = testr[i]

    return shared_f_from_p1, shared_r_from_p1

def final_primer(shared_f, shared_r, fp, rp, seq):
    primers = ["",""]
    rcandi = {}
    minl = 210
    maxl = 370
#    print len(shared_f)
    if (len(shared_f) > 0):
        #print shared_f
        #print "this is shared"
        #print shared_f
        for item in shared_f.items():
            start =  seq.find(item[0])
            for x in rp:
                end = seq.find(x)+len(x)
                le = end - start
                if(le > minl and le < maxl):
                    rcandi[x] = le
            #print rcandi
            rfi = ""
            rfile = 5000
            for y in rcandi.items():
                if(y[1] < rfile):
                    rfile = y[1]
                    rfi = y[0]
                    primers = [item[0],y[0]]
    else:
        fle = 5000
        #print fp, rp
        for f in fp:
            start = seq.find(f)
            #print start
            for r in rp:
                end = seq.find(r)+len(r)
                le = end - start
                #print end, le
                if (le < fle and le > minl and le < maxl):
                    primers = [f, r]

    return primers

def find_least_primer_two_gene(g1,g2,faseq,primer,genename):
    seq1 = faseq[g1]
    fp = primer[g1][0]
    rp = primer[g1][1]
    seq2 = faseq[g2]
    fp2 = primer[g2][0]
    rp2 = primer[g2][1]
    shared_f_from_p1, shared_r_from_p1 = find_share(fp,rp,seq1,seq2)
    shared_f_from_p2, shared_r_from_p2 = find_share(fp2,rp2,seq1,seq2)
    shared_f, shared_r = merge(shared_f_from_p1, shared_r_from_p1,shared_f_from_p2, shared_r_from_p2)

    seq1_primers = final_primer(shared_f, shared_r, fp, rp, seq1)
    seq2_primers = final_primer(shared_f, shared_r, fp2, rp2, seq2)
    result1 = [genename, g1,seq1_primers[0], seq1_primers[1]]
    result2 = [genename, g2,seq2_primers[0], seq2_primers[1]]

#    if(genename == "H-NS"):
#        print shared_f, shared_r, fp, rp, seq1
    
    if(result1[2] == result2[2]):
        result2[2] = "-"
    print '\t'.join(result1)
    print '\t'.join(result2)

def find_lease_primer_one_gene(g1,faseq,primer,genename):
    shared_f = {}
    shared_r = {}
    fp = primer[g1][0]
    rp = primer[g1][1]
    seq = faseq[g1]
    seq_primers = final_primer(shared_f, shared_r, fp, rp, seq)
    result = [genename, g1, seq_primers[0], seq_primers[1]]
    print '\t'.join(result)

def main():
    #read list
    list_gene = {}
    for line in open(sys.argv[1],'r'):
        spl = line.strip().split('\t')
        if(list_gene.has_key(spl[2])):
            temp = list_gene[spl[2]]
            temp.append(spl[1])
            list_gene[spl[2]] = temp
        else:
            temp = [spl[1]]
            list_gene[spl[2]] = temp

    #read fasta
    fafile = sys.argv[2]
    faseq = utils.read_fasta_usda(fafile)

    #read primers -> primer
    mypath = sys.argv[3]
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    primer = {}
    for file in onlyfiles:
        if (file[:1] == "."):
            continue
        fullpath = mypath+file
        fpri,rpri = utils.read_trad_primer(fullpath)
        locus = file.split('.')[0]
        if(primer.has_key(locus)):
            temp = primer[locus]
            temp.append([fpri,rpri])
            primer[locus] = temp
        else:
            primer[locus] = [fpri,rpri]
    
#    print list_gene
    for item in list_gene.items():                                                                      
        if(len(item[1]) >1):
            genename = item[0]
            g1 = item[1][0]
            g2 = item[1][1]
            if( primer.has_key(g1) and primer.has_key(g2)):
                find_least_primer_two_gene(g1,g2,faseq,primer,genename)
            #else:
            #    print g1,g2
        else:
            genename = item[0]
            g1 = item[1][0]
            if(primer.has_key(g1)):
                find_lease_primer_one_gene(g1,faseq,primer,genename)
            #else:
            #    print g1

    

if __name__ == '__main__':
    main()

