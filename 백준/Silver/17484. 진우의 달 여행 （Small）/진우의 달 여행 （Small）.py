[N,M],*b=[[*map(int,i.split())]for i in open(0)]

v=[3*[0]for _ in[0]*M]
for i in b:
    t=[3*[float('inf')]for _ in[0]*M]
    for c in range(M):
        for dc in-1,0,1:
            nc=c+dc
            for j in-1,0,1:
                if 0<=nc<M and j!=dc:
                    t[nc][dc]=min(t[nc][dc],v[c][j]+i[c])
    v=t
print(min(sum(v,[])))