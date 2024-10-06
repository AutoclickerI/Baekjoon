import sys
input=lambda:sys.stdin.readline()[:-1]
for i in[0]*int(input()):
    for s in[input()for _ in[0]*int(input())][1:]:
        if s=='111':
            i^=2
        if s in('011','110'):
            i^=1
    print('YNeosnyoe s'[i<1::2])