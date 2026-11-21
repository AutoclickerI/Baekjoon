N,M,K=map(int,input().split())
import math
K-=0<K
y,x=K//M,K%M
print(math.comb(x+y,x)*math.comb(N+~y+M+~x,M+~x))