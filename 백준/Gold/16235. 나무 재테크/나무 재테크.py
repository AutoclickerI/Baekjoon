N,M,K,*A=map(int,open(0).read().split())
b=N*N*[5]
z=[[]for _ in[0]*N*N]
for y,x,c in zip(*3*[iter(A[-3*M:])]):z[(y-1)*N+x-1]+=c,
for _ in[0]*K:
    t=[[]for _ in[0]*N*N]
    for v in range(N*N):
        a=0
        for i in sorted(z[v]):
            if b[v]<i:a+=i//2
            else:
                b[v]-=i;t[v]+=i+1,
                if i%5==4:
                    for dy,dx in(-1,0),(0,1),(-1,1),(-1,-1),(0,-1),(1,-1),(1,0),(1,1):
                        ny,nx=v//N+dy,v%N+dx
                        if 0<=ny<N and 0<=nx<N:t[ny*N+nx]+=1,
        b[v]+=A[v]+a
    z=t
print(sum(map(len,z)))