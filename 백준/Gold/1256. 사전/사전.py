from math import*
N,M,K=map(int,input().split())
r=''
p=(K<=comb(v:=N+M,M))*v
while p:c=comb(p:=p-1,M);r+='az'[w:=c<K];M-=w;K-=c*w
print(r or-1)