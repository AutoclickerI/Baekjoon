N,T=map(int,input().split())
A=0,*map(int,input().split())
cur=time=1
visited=[0]*-~N
while T:
    T-=1
    if visited[cur]:
        T%=time-visited[cur]
        visited=[0]*-~N
    visited[cur]=time
    cur=A[cur]
    time+=1
print(cur)