import sys
input=lambda:sys.stdin.readline()[:-1]

for _ in[0]*int(input()):
    n=int(input())
    d=set()
    v=set()
    f=0
    for _ in[0]*n:
        s=input()
        v|={s[:i]for i in range(1,len(s))}
        d|={s}
    if v&d:f=1
    print('YNEOS'[f::2])