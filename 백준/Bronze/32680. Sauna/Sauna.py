_,*l=map(int,open(0).read().split())
m=max(l[::2])
print(*[M:=min(l[1::2])+1-m,m]*(0<M)or['bad news'])