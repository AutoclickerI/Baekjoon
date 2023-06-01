from math import*
N,K,M=map(int,input().split())
l=[]
while N*K!=0:l+=[[N%M,K%M]];N//=M;K//=M
a=1
for p,q in l:a*=comb(p,q)
print(a%M)