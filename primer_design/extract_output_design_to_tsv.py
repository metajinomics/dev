#extract output from primer design 
#python extract_output.py input > output
#this output make primer for convential qPCR primer (NOT Truseq)
import sys

def main():
    num = 0
    file = sys.argv[1]
    for line in open(file,'r'):
        if line[:13] == "Primer Pair: " :
            num += 1
            f = []
            r= []
            spl = line.strip().split("revOligo")
            for i in range(0,len(spl)):
                oli =  spl[i].split("seq=")
                snum = 0
                for j in range(1,len(oli)):
                    snum += 1
                    oneoli = oli[j].split("}")
                    if( i == 0):
                        f.append(oneoli[0])
                    else:
                        r.append(oneoli[0])
            if len(f) >= len(r):
                for i in range(0,len(f)):
                    rpri = ""
                    set = str(num)+"_"+str(i+1)
                    if(i+1 > len(r)):
                        rpri = "_"
                    else:
                        rpri = r[i]
                    print "%s\t%s\t%s\t%s" %(file.split('.')[0],set,f[i],rpri)
            else:
                for i in range(0,len(r)):
                    fpri = ""
                    set = str(num)+"_"+str(i+1)
                    if(i+1 > len(f)):
                        fpri = "_"
                    else:
                        fpri = f[i]
                    print "%s\t%s\t%s\t%s" %(file.split('.')[0],set,fpri,r[i])

if __name__ == '__main__':
    main()
