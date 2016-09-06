#extact output from primer design program
#python extract_output.py primers.txt 90 truseq

import sys
import reverse_complement
def get_primers(i,con,iter,fname,rc):
    k=1
    for j in range(0,iter*2+1):
        line = con[i+j]
        if (line[2:14]=="Primer Pair:"):
            spl = line.split("Oligo{seq=")
            fw = spl[1].split('}')[0]
            rev = spl[2].split('}')[0]
            if (rc == 1):
                revrc = reverse_complement.get_rc(rev)
            else:
                revrc = rev
            print ">F:"+fname.split('.')[0]+'_'+str(k)
            print fw
            print ">R:"+fname.split('.')[0]+'_'+str(k)
            print revrc
            k += 1
    
cut = float(sys.argv[2])/100
prev = ""
fread = open(sys.argv[1])
fname = sys.argv[1]
con = fread.readlines()
if(sys.argv[3] == 'truseq'):
    rc = 1
else:
    rc = 0
i = 0
for line in con:
    if(line[:22] == 'Percent Seq Coverage: '):
        spl = line.split(': ')
        per = float(spl[1])
        if(per > cut):
            iter =  int(prev.split(' ')[0])
            get_primers(i,con,iter,fname,rc)
            break
    #if no result until 20 primers then print 20 primers 
    elif (line[:15] == '20 Primer Pair:'):
        iter = 20
        i += 1
        get_primers(i,con,iter,fname,rc)
    prev = line.strip()
    i += 1
