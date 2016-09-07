#find primer missing error
#python find_miss_primer.py design.txt
#for x in *.design.txt;do python /Users/jinchoi/Box\ Sync/Github/metajinomics/dev/primer_design/find_miss_primer.py $x;done
import sys
flag = 0
li = []
for line in open(sys.argv[1],'r'):
    if(line[:14] == "1 Primer Pair:"):
        flag = 1
    if(flag == 1 and line.strip() != ""):
        li.append(line.strip())
    elif(flag == 1 and line.strip() == ""):
        break

if(len(li) == 2):
    print sys.argv[1]
