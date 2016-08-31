import reverse_complement

def read_map(filename):
    dict={}
    for line in open(filename,'r'):
        spl = line.strip().split('\t')
        dict[spl[1]] = spl[0]
    return dict

def get_target_seq(locus,filename):
    flag = 0
    seq = ""
    for line in open(filename,'r'):
        if(line[:1] == ">"):
            spl = line.split(' ')
            if (locus == spl[0][1:]):
                flag = 1
        elif(line[:1] != ">" and flag == 1):
            seq = line.strip()
            return seq
            flag = 0
    return seq

def get_target(fpri,rpri,ori):
    target = ""
    rev = reverse_complement.get_rc(rpri)
    for item in ori.items():
        if(fpri in item[1] and rev in item[1]):
            target = item[1]
    return target

def make_primer3_input(fprimer,rprimer,target,gene,num):
    fwrite = open(num+gene+".primer3input.txt",'w')
    fwrite.write("SEQUENCE_TEMPLATE="+target+'\n')
    fwrite.write("SEQUENCE_PRIMER="+fprimer+'\n')
    fwrite.write("SEQUENCE_PRIMER_REVCOMP="+rprimer+'\n')
    default = open("/Users/jinchoi/programs/primer3-2.3.7/primer3_default_template.txt",'r')
    for line in default:
        fwrite.write(line)
    return

def make_primer3_input_design(fp,rp,target,iter):
    fwrite = open("./"+str(iter)+"primer3input.txt",'w')
    fwrite.write("SEQUENCE_TEMPLATE="+target+'\n')
    start = 100
    end = 500
    if(int(fp) < 100):
        start = 0
    if(int(fp)+500 > len(target)):
        end = len(target) - int(fp)
    fwrite.write("SEQUENCE_INCLUDED_REGION="+str(int(fp)-start)+','+str(end)+'\n')
    default = open("/Users/jinchoi/programs/primer3-2.3.7/primer3_default_template2.txt",'r')
    for line in default:
        fwrite.write(line)
    return


def read_fasta(filename):
    fread = open(filename,'r')
    dict = {} 
    name = ""
    flag = 0
    for line in fread:
        if(line[:1] == ">"):
            name = line.strip()
        else:
            if(dict.has_key(name)):
                temp = dict[name]
                temp = temp + line.strip()
                dict[name] = temp
            else:
                dict[name] = line.strip()
    return dict

def get_primers(i,con,iter,rc):
    k=1
    fprim = []
    rprim = []
    fp = []
    rp = []
    for j in range(0,iter*2+1):
        line = con[i+j]
        if (line[2:25]=="Primer Pair: PrimerPair" or line[3:26] == "Primer Pair: PrimerPair"):
            spl = line.split("Oligo{seq=")
            loc = line.split("[")[1].split(', ')
            fp.append(loc[0])
            rp.append(loc[1].split(']')[0])
            fw = spl[1].split('}')[0]
            rev = spl[2].split('}')[0]
            if (rc == 1):
                revrc = reverse_complement.get_rc(rev)
            else:
                revrc = rev

            fprim.append(fw)
            rprim.append(revrc)
            k += 1
        elif(line.strip() == ""):
            break
    return fprim,rprim,fp,rp
   

def read_primer_out(filename):
    fread = open(filename,'r')
    con = fread.readlines()
    cut = 0.9
    primer = []
    prev = ""
    i = 0
    rc = 0
    for line in con:
        if(line[:22] == 'Percent Seq Coverage: '):
            spl = line.split(': ')
            per = float(spl[1])
            if(per > cut):
                iter =  int(prev.split(' ')[0])
                fprim,rprim,fp,rp = get_primers(i,con,iter,rc)
                break
        prev = line.strip()
        i += 1
    primer = [fprim,rprim,fp,rp]
    return primer
