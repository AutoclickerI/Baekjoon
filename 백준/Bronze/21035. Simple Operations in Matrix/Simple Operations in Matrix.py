N,M=map(int,input().split())
mat=[[*map(int,input().split())]for _ in[0]*N]
for _ in[0]*int(input()):
    p,q,r=input().split()
    if p[0]=='r':
        for i in range(M):mat[int(q)-1][i]+=int(r)
    else:
        for i in range(N):mat[i][int(q)-1]+=int(r)
mat=sum(mat,[])
print(sum(mat),min(mat),max(mat))