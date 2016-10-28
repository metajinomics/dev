
#find which primer is used
#python find_primer.py primer seq

import sys
import utils
import reverse_complement

def mismatch(str1, str2, alow):
    mis = 0
    for i in range(0,len(str1)):
        if(str1[i] != str2[i]):
            mis += 1
            if (mis > alow):
                return False
    return True

def main():
    min = 210
    max = 370
    #parameters that used
    mis = 0
    #read primer
    fpri, rpri = utils.read_trad_primer(sys.argv[1])
    lfile = sys.argv[2]
    num = 0
    seq = utils.read_fasta(sys.argv[2])
    for item in seq.items():
        se = item[1]
        for f in fpri:
            for i in range(0, len(se)-len(f)):
                str1 = se[i:len(f)+i]
                #print str1, f
                #print mismatch(str1,f,mis)
                if mismatch(str1,f,mis):
                    #print "match"
                    num += 1
                    output = ">F:"+lfile+"_"+str(num)+"\n"+f+'\n'
                    #print output
                    #print ">F:",f, i
                    for r in rpri:
                        rp = r
                        for j in range(0, len(se)-len(rp)):
                            str2 = se[j:len(rp)+j]
                            if mismatch(str2,rp,mis):
                                #print "match"
                                frp = reverse_complement.get_rc(rp)
                                #print ">R:",frp,j+len(rp), j+len(rp)-i
                                flen = j+len(rp)-i
                                #print flen
                                if(flen >min and flen<max):
                                    output = output + ">R:"+lfile+"_"+str(num)+"\n"+frp+'\n'
                                    print output

if __name__ == '__main__':
    main()
