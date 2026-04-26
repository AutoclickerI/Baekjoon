import sys
input=sys.stdin.readline

for T in range(int(input())):
    N=int(input())
    ma=mb=mc=f=0
    for i in range(N):
        a,b,c,p=map(int,input().split())
        ma=max(ma,a)
        mb=max(mb,b)
        mc=max(mc,c)
        f|=p<ma+mb+mc+i+1
    print('YNEOS'[f::2])