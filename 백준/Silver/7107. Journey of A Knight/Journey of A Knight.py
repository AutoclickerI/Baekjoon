N,M,I,J=map(int,input().split())
visited=[[0]*M for _ in[0]*N]
from collections import deque
dq=deque([(0,0,0)])
visited[0][0]=1
while dq:
    p,q,cnt=dq.popleft()
    if p==I-1 and q==J-1:
        print(cnt)
        exit()
    for i,j in zip([-1,1,-2,2]*2,[2,2,1,1,-2,-2,-1,-1]):
        if 0<=p+i<N and 0<=q+j<M and visited[p+i][q+j]==0:
            visited[p+i][q+j]=1
            dq.append((p+i,q+j,cnt+1))
print('NEVAR')