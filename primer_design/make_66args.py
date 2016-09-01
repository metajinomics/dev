#

import sys
import os
dict = {}
for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    if(len(spl) == 2):
        dict[spl[0]] = [spl[1].split(':')[0]]
    else:
        dict[spl[0]] = [spl[1].split(':')[0],spl[2].split(':')[0]]

#print dict
ls = os.listdir('.')
#print ls

for item in dict.items():
    fwrite = open(item[0]+'.arg.fa','w')
    for x in item[1]:
        for y in ls:
            if(x in y):
                fread = open(y,'r')
                for line in fread:
                    fwrite.write(line)
