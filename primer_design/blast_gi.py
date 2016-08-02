#this script generate splited gi file from blast output
#python blast_gi.py blast.output > gi.txt
import sys
fwrite = open('map_file.txt','w')
cid = ""
i = 1
for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    ids = spl[1].split('|')[1]
    if not(cid == spl[0]):
        fwrite.write("gene"+str(i)+'\t'+spl[0]+'\n')
        file = open("gene"+str(i)+'.txt','w')
        if (int(spl[8]) < int(spl[9])):
            file.write(ids+'\t'+spl[8]+'-'+spl[9]+'\n')
        cid = spl[0]
        i += 1
    else:
        if (int(spl[8]) < int(spl[9])):
            file.write(ids+'\t'+spl[8]+'-'+spl[9]+'\n')
