def inner_loop(N,depth):
    if depth==1:
        for i in range(N+1):
            yield i,
    else:
        for i in range(N+1):
            for j in inner_loop(i,depth-1):
                yield *j,i
import math
N,M=map(int,input().split())
s=tuple(map(int,input()))[::-1]
sl=tuple(sorted(s))
ans=0
l=[]
for i in inner_loop(M,N):
    if i==sl:
        break
    d={}
    for j in i:
        d[j]=d.get(j,0)+1
    t=N
    a=1
    for i in d:
        a*=math.comb(t,d[i])
        t-=d[i]
    ans+=a
from itertools import*
for i in{*permutations(i)}:ans+=i[::-1]<s
print(ans)