N,M,K=map(int,input().split())

b=[input()for _ in[0]*N]

def to_4d(val):
    f=val%2
    val//=2
    k=val%(K+1)
    val//=K+1
    x=val%M
    val//=M
    return val,x,k,f

def to_1d(y,x,k,f):
    return((y*M+x)*(K+1)+k)*2+f

v=[float('inf')for _ in[0]*2*-~K*M*N]

v[0]=0

from collections import deque

dq=deque([(0,0)])

while dq:
    val,c=dq.popleft()
    y,x,k,f=to_4d(val)
    if v[to_1d(y,x,k,f)]<c:
        continue
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=nx<M and 0<=ny<N:
            if b[ny][nx]=='0'and c+1<v[to_1d(ny,nx,k,1-f)]:
                v[to_1d(ny,nx,k,1-f)]=c+1
                dq+=(to_1d(ny,nx,k,1-f),c+1),
            if b[ny][nx]=='1'and k+1<=K and c+1<v[to_1d(ny,nx,k+1,1-f)]:
                if f:
                    if c+1<v[to_1d(y,x,k,1-f)]:
                        v[to_1d(y,x,k,1-f)]=c+1
                        dq+=(to_1d(y,x,k,1-f),c+1),
                else:
                    v[to_1d(ny,nx,k+1,1-f)]=c+1
                    dq+=(to_1d(ny,nx,k+1,1-f),c+1),

z=min(v[-2*(K+1):])+1
print(-(z==float('inf'))or z)