N,*l=map(int,open(0).read().split())
d=~N*~N*[N]
for v in range(N*N):i,j=v//N,v%N;d[(i+1)*(N+1)+j+1]=[min(d[(i+1)*(N+1)+j],d[v+i+1]),d[v+i]-1][l[i]==l[~j]]
print(d[-1])