N,*l,K=map(int,open(i:=0).read().split())
while i<N:print(*sorted(l[i:(i:=i+N//K)]))