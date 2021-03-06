
import sys
import reverse_complement
prim = {}

genename = sys.argv[1].split('.')[0]
swi = 0
gene = ""
for line in open(sys.argv[1],'r'):
    if(line[:1] == ">"):
        gene = line.strip()[3:]
        if not prim.has_key(gene):
            prim[gene]={}
        if(line[1:2] == "F"):
            swi = 0
        elif (line[1:2] == "R"):
            swi = 1
        else:
            print "direction needed"
            sys.exit(0)
    else:
        if(swi == 0):
            temp =prim[gene]
            temp['f'] = line.strip()
            prim[gene]=temp
        else:
            temp=prim[gene]
            temp['r'] = line.strip()
            prim[gene]=temp

for item in prim.items():
    print '\t'.join([genename,item[0],prim[item[0]]['f'],prim[item[0]]['r']])
#
#if(len(prim['f']) > len(prim['r'])):
#    for i in range(0,len(prim['f'])):
#        if(i>=len(prim['r'])):
#            r = "-"
#        else:
#            r = reverse_complement.get_rc(prim['r'][i])
#        f = prim['f'][i]
#        print genename+'\t'+genename+'\t'+f+'\t'+r
#else:
#    for i in range(0,len(prim['r'])):
#        if(i>=len(prim['f'])):
#            f = "-"
#        else:
#            f = prim['f'][i]
#        r = reverse_complement.get_rc(prim['r'][i])
#        print genename+'\t'+genename+'\t'+f+'\t'+r
