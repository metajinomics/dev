#!/usr/bin/python
#python add_anno.py normal_counts.txt mgm4675652.3_organism_KEGG_nopipe.tab mgm4675652.3_function_KEGG_nopipe.tab new_big_table.txt
import sys
import mg_rast_jason
import taxonomy_finder
#read mgm
mgm = open(sys.argv[3],'r')
#put in dictionary, if same, use low e value
dict = {}
next(mgm)
for line in mgm:
    splt = line.strip().split('\t')
    if(len(splt)>2):
        if(dict.has_key(splt[0])):
            if(float(dict[splt[0]][1]) < float(splt[11])):
                dict[splt[0]] = [splt[1],splt[11],splt[12]]
        else:
            dict[splt[0]] = [splt[1],splt[11],splt[12]]
mgm.close()

ormgm = open(sys.argv[2],'r')
#put in dictionary, if same, use low e value                                                           
ordict = {}
next(ormgm)
for line in ormgm:
    splt = line.strip().split('\t')
    if(len(splt)>2):
        if(ordict.has_key(splt[0])):
            if(float(ordict[splt[0]][1]) < float(splt[11])):
                ordict[splt[0]] = [splt[1],splt[11],splt[12]]
        else:
            ordict[splt[0]] = [splt[1],splt[11],splt[12]]
ormgm.close()


#print len(dict)
#process normal_counts
count = open(sys.argv[1],'r')
fwrite = open(sys.argv[4],'w')
lines = count.next()
fwrite.write(lines.strip()+'\t'+'organism'+'\t'+'function'+'\t'+'ec'+'\t'+'full_tax'+'\n')
for line in count:
    splt = line.strip().split('\t')
    organism = "null"
    function = "null"
    ecnum = "null"
    fulltax = "null"
    if(dict.has_key(splt[0])):
        md5 = dict[splt[0]][0]
        function =  dict[splt[0]][2]
        ecs = function.split("EC:")
        if(len(ecs)>1):
            ec = ecs[1].split(")")
            ecnum = ec[0]

    if(ordict.has_key(splt[0])):
        organism = ordict[splt[0]][2]
        taxid = mg_rast_jason.get_taxid(md5)
        if(str(taxid)!="null"):
            fulltax = taxonomy_finder.from_id(str(taxid)) 

    fwrite.write(line.strip()+'\t'+ organism+'\t' + function+'\t'+ecnum+'\t'+fulltax+'\n')
    
