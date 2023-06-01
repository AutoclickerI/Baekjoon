import math
N,K=map(int,input().split())
M=10**9+7
l=[]
while N*K:l+=[[N%M,K%M]];N//=M;K//=M
a=1
for p,q in l:a*=math.comb(p,q)
print(a%M)