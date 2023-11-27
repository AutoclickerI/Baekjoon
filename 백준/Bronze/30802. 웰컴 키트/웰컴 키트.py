N,*l,T,P=map(int,open(0).read().split())
print(-sum(i//-T for i in l),*divmod(N,P))