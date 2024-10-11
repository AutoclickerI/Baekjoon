from itertools import*
for s in[0]*int(input()):
    N=int(input());c=0
    for i in cycle([*map(int,input().split())]):
        if c+i<=N:c+=i;s+=c
        if c==N:break
    print(s)