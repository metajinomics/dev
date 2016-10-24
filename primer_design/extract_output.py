#extract output from primer design 
#python extract_output.py input > output

import sys


def main():
    num = 0
    for line in open(sys.argv[1],'r'):
        if line[:13] == "Primer Pair: " :
            num += 1
            spl = line.strip().split("revOligo")
            for i in range(0,len(spl)):
                oli =  spl[i].split("seq=")
                snum = 0
                for j in range(1,len(oli)):
                    snum += 1
                    oneoli = oli[j].split("}")
                    if( i == 0):
                        print ">F:"+str(num)+"_"+str(snum)
                    else:
                        print ">R:"+str(num)+"_"+str(snum)
                    print oneoli[0]

if __name__ == '__main__':
    main()
