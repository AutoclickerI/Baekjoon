import math
K,N=map(int,input().split())
v=N+K-1>>1
print(sum(math.comb(N,i)for i in range(max(0,v-K+1),v+1)))