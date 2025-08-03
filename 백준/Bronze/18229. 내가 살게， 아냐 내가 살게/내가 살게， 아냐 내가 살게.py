(N,M,K),*l=[[*map(int,i.split())]for i in open(0)]
r=[0]*N
for j in range(M):
 for i in range(N):r[i]+=l[i][j];K<=r[i]<exit(print(i+1,j+1))