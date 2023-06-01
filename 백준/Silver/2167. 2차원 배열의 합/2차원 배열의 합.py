p,q=map(int,input().split())
l=[[*map(int,input().split())]for _ in[0]*p]
L=[[0]*(q+1)for _ in[0]*(p+1)]
for i in range(p):
    for j in range(q):L[i+1][j+1]=L[i][j+1]+L[i+1][j]+l[i][j]-L[i][j]
for _ in[0]*int(input()):
    p,q,r,s=map(int,input().split())
    print(L[r][s]-L[p-1][s]-L[r][q-1]+L[p-1][q-1])