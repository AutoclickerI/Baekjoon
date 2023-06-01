import math
C=math.comb
N,M,K=map(int,input().split())
print(sum(C(M,i)*C(N-M,M-i)/C(N,M)for i in range(K,M+1)))