n,m,*T=map(int,open(0).read().split())
print(max([v:=sum(T[:m])]+[v:=v+i-j for i,j in zip(T[m:],T)]))