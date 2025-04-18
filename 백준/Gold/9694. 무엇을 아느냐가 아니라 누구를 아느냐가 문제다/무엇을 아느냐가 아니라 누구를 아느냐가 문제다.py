from heapq import*

for T in range(int(input())):
    M,N=map(int,input().split())
    edges=[[]for _ in[0]*N]
    v=[(float('inf'),-1)]*N
    for _ in[0]*M:
        s,e,m=map(int,input().split())
        edges[s]+=(e,m),
        edges[e]+=(s,m),
    v[0]=0,0
    hq=[(0,0)]
    while hq:
        c,n=heappop(hq)
        for e,m in edges[n]:
            if c+m<v[e][0]:
                v[e]=(c+m,n)
                heappush(hq,(c+m,e))
    
    a=[N-1]
    while 0<a[-1]:
        a+=v[a[-1]][1],
    a=a[::-1]
    if a[0]<0:a.pop()
    print(f'Case #{T+1}:',*a)