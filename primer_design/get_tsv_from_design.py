
import sys
import reverse_complement
tru = 1

def main():
    num = 0
    file = sys.argv[1]
    set = 0
    for line in open(file,'r'):
        genename = file.split('.')[0]
        if line[:13] == "Primer Pair: " :
            set += 1
            prim = {}
            prim['f'] = []
            prim['r'] = []
            num += 1
            spl = line.strip().split("revOligo")
            for i in range(0,len(spl)):
                oli =  spl[i].split("seq=")
                snum = 0
                for j in range(1,len(oli)):
                    snum += 1
                    oneoli = oli[j].split("}")
                    if( i == 0):
                        #print ">F:"+file+"_"+str(num)+"_"+str(snum)
                        prim['f'].append(oneoli[0])
                    else:
                        #print ">R:"+file+"_"+str(num)+"_"+str(snum)
                        prim['r'].append(oneoli[0])
                    #print oneoli[0]
            #print prim
            for i in range(0,len(prim['f'])):
                r = reverse_complement.get_rc(prim['r'][i])
                print genename+"\t"+str(set)+"_"+str(i+1)+"\t"+prim['f'][i]+"\t"+ r

if __name__ == '__main__':
    main()
