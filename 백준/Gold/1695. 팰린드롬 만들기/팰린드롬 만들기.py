N,*l=map(int,open(0).read().split())
d=~N*~N*[N]
for v in range(N*N):i=v//N;d[v+N+i+2]=min(d[v+N-~i],d[v-~i],d[v+i]-(l[i]==l[-v%N-1]))
print(d[-1])