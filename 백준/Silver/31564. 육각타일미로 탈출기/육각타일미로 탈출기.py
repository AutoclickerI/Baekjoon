from collections import deque
dq=deque([(0,0,0)])
N,M,K=map(int,input().split())
V=[M*[1]for _ in[0]*N]
for _ in[0]*K:
    p,q=map(int,input().split())
    V[p][q]=0
while dq:
    y,x,t=dq.popleft()
    (y,x)==(N-1,M-1)<exit(print(t))
    for dy,dx in(1,0),(-1,0),(0,1),(0,-1),(1,y%2*2-1),(-1,y%2*2-1):
        if N>y+dy>=0<=x+dx<M and V[y+dy][x+dx]:
            V[y+dy][x+dx]=0
            dq.append((y+dy,x+dx,t+1))
print(-1)