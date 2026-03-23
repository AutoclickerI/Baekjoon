[M,N],*l=[map(int,i.split())for i in open(0)]
jl=[0]*2*M
for a,b,c in l:
    jl[a]+=1
    jl[a+b]+=1

for i in range(1,2*M):
    jl[i]+=jl[i-1]
addr=[M*[0]for _ in[0]*M]
for i in range(M):
    addr[~i][0]=jl[i]+1
for i in range(M,2*M-1):
    addr[0][i-M+1]=jl[i]+1
for y in range(1,M):
    for x in range(1,M):
        addr[y][x]=max(addr[y][x-1],addr[y-1][x-1],addr[y-1][x])
for i in addr:print(*i)