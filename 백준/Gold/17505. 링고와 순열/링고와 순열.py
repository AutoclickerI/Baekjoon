N,K=map(int,input().split())
l=[]
for i in range(N)[::-1]:
    l+=K>=i,
    if K>=i:K-=i
l=l[::-1]
from collections import deque
dq=deque()
for i,j in zip(l,range(N)):
    if i:
        dq.appendleft(j+1)
    else:
        dq.append(j+1)
print(*dq)