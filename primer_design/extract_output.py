import sys
for line in open(sys.argv[1]):
    if(line[:22] == 'Percent Seq Coverage: '):
        spl = line.split(': ')
        per = float(spl[1])
        if(per > 0.9):
        print per
