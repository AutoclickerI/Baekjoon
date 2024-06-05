X,Y,K,M=map(int,input().split())
m=M
d={(0,0)}
from collections import deque
dq=deque([(0,0,0)])
k=0
while dq:
    p,q,k=dq.popleft()
    if K<=k:break
    for i in(p,Y),(X,q),(p,0),(0,q),(max(p+q-Y,0),min(Y,p+q)),(min(p+q,X),max(0,p+q-X)):
        if i not in d:
            d.add(i)
            m=min(abs(sum(i)-M),m)
            dq+=(*i,k+1),
print(m)