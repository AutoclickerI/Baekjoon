import sys
input=sys.stdin.readline

from bisect import*
for T in range(int(input())):
    n=int(input())
    *l,=map(int,input().split())
    d=[0]
    c=[-2e+9]
    for i in l:
        if c[-1]<i:
            d+=[len(c)]
            c+=[i]
        else:
            d+=[L:=bisect_left(c,i)]
            c[L]=i
    
    d2=[0]
    c=[-2e+9]
    for i in l[::-1]:
        if c[-1]<i:
            d2+=[len(c)]
            c+=[i]
        else:
            d2+=[L:=bisect_left(c,i)]
            c[L]=i
    d2=d2[::-1]
    
    print(max([0]+[i+j-1 for i,j in zip(d[1:],d2[:-1])if j>1<i]))