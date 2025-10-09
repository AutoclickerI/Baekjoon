N,M,K=map(int,input().split())
A=sum([[*map(int,input().split())]for _ in[0]*N],[])

b=N*N*[5]

trees=[[]for _ in[0]*N*N]

for _ in[0]*M:
    y,x,c=map(int,input().split())
    trees[(y-1)*N+x-1]+=c,

for _ in[0]*K:
    t=[[]for _ in[0]*N*N]
    for idx in range(N*N):
        add=0
        trees[idx].sort()
        for i in trees[idx]:
            if b[idx]<i:
                add+=i//2
            else:
                b[idx]-=i
                t[idx]+=i+1,
                if i%5==4:
                    for dy,dx in(-1,0),(0,1),(-1,1),(-1,-1),(0,-1),(1,-1),(1,0),(1,1):
                        ny,nx=idx//N+dy,idx%N+dx
                        if 0<=ny<N and 0<=nx<N:
                            t[ny*N+nx]+=1,
        b[idx]+=A[idx]+add
    trees=t

print(sum(len(i)for i in trees))