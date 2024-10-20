import math

d={}

m=10**9+7

def f(n,k):
    if(n,k)in d:
        return d[n,k]
    if n==1:
        return 1
    else:
        ret=pow(n,k,m)
        for i in range(1,n):
            ret-=f(i,k)*math.comb(n,i)
        d[n,k]=ret%m
        return d[n,k]

for T in range(int(input())):
    print(f'Case #{T+1}:',f(*map(int,input().split())))