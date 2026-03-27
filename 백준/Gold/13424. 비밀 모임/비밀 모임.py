for _ in[0]*int(input()):
    N,M=map(int,input().split())
    N+=1
    b=[N*[float('inf')]for _ in[0]*N]
    for i in range(N):b[i][i]=0
    for _ in[0]*M:
        s,e,c=map(int,input().split())
        b[s][e]=b[e][s]=c
    for m in range(N):
        for s in range(N):
            for e in range(N):
                b[s][e]=min(b[s][e],b[s][m]+b[m][e])
    input()
    v=[0]*N
    for i in map(int,input().split()):
        for j in range(N):
            v[j]+=b[i][j]
    print(v.index(min(v)))