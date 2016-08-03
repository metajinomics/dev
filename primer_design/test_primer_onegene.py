#this script test primer

#python test_primer_onegene.py primer.txt gene.fa

import sys
import reverse_complement
import os
def make_primer3_input(fprimer,rprimer,target):
    fwrite = open("test.primer3input.txt",'w')
    fwrite.write("SEQUENCE_TEMPLATE="+target+'\n')
    fwrite.write("SEQUENCE_PRIMER="+fprimer+'\n')
    fwrite.write("SEQUENCE_PRIMER_REVCOMP="+rprimer+'\n')
    default = open("/home/ubuntu/primer3-2.3.7/primer3_default_template.txt",'r')
    for line in default:
        fwrite.write(line)
    return

def get_target(tempseq,fprimer,rprimer):
    seq = ''.join(tempseq)
    rprimer = reverse_complement.get_rc(rprimer)
    if(fprimer in seq and rprimer in seq and seq.find(fprimer) < seq.find(rprimer)):
        return 1
    else:
        return 0

#read primers
fprimer = ""
rprimer = ""
flag = ""
for line in open(sys.argv[1],'r'):
    if (line[1:2]=="F"):
        flag = "F"
    elif (line[1:2]=="R"):
        flag = "R"
    else:
        if(flag == "F"):
            fprimer = line.strip()
            flag = ""
        elif (flag == "R"):
            rprimer = line.strip()
            flag = ""
        else:
            flag = ""
    
print fprimer
print rprimer
#read target gene
target = ""
tempseq = []
first = 0
for line in open(sys.argv[2],'r'):
    if(line[:1]==">" and first == 0):
        first = 1
        continue
    elif (line[:1] == ">" and first ==1):
        if (get_target(tempseq,fprimer,rprimer)):
            target = ''.join(tempseq)
            break
        tempseq = []
    else:
        tempseq.append(line.strip())

print target
#make primer3 input
make_primer3_input(fprimer,rprimer,target)

#run primer3
os.system("/home/ubuntu/primer3-2.3.7/src/primer3_core < test.primer3input.txt -strict_tags -output=./test.out.txt")

#check if there are error
outread = open("test.out.txt",'r')
flag = 0
for line in outread:
    if("ERROR" in line):
        print "error"
        print line,
        flag = 1
    elif("PROBLEMS" in line):
        print "problem"
        print line,
        flag = 1
if (flag == 0):
    print "no problem"
    
