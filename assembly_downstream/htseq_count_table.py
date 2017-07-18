#!/usr/bin/python

import sys

def main():
    list_id = []
    count = {}
    for n, filename in enumerate(sys.argv[1:]):
        for line in open(filename,'r'):
            spl = line.strip().split('\t')
            if n == 0:
                list_id.append(spl[0])
            if count.has_key(spl[0]):
                count[spl[0]] = count[spl[0]].append(spl[1])
            else:
                count[spl[0]] = [spl[1]]
    for ids in list_id:
        result = [ids] + count[ids]
        print '\t'.join(result)


if __name__ == '__main__':
    main()
