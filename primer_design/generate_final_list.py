#generage final primer list
# gene org trueseq_f truseq_r expected_length
# gene org conventional_pcr_f conventional_pcr_r expected_length

#python generage_final_list.py list map check_match truseq > output

import sys
import utils
import reverse_complement

def show_list(gene,target,map,match):
    org = map[target]
    prod = []
    for item in match.items():
        if(target in item[0]):
            prod = item[1]

    for x in prod:
        spl = x.split(' ')
        fpri = spl[0]
        rpri = ''
        exp = spl[2]
        if(sys.argv[4] == "truseq"):
            rpri = reverse_complement.get_rc(spl[1])
        else:
            rpri = spl[1]
        if(int(exp) > 200):
            result = [gene,org,fpri,rpri,exp]
            print '\t'.join(result)

def main():
    #read list
    li = utils.read_arg_list_all(sys.argv[1])

    #read map
    map = utils.read_map(sys.argv[2])
    #read check_match
    match = utils.read_check_match(sys.argv[3])
    if(sys.argv[4] == "truseq"):
        print 'gene\torg\ttruseq_f\ttruseq_r\texpected_length'
    else:
        print 'gene\torg\tconventional_pcr_f\tconventional_pcr_r\texpected_length'
    for x in li:
        gene = x[0]
    
        if(len(x) == 2):
            target1 = x[1]
            show_list(gene,target1,map,match)
            
        else:
            target1 = x[1]
            target2 = x[2]
            show_list(gene,target1,map,match)
            show_list(gene,target2,map,match)

if __name__ == '__main__':
    main()
