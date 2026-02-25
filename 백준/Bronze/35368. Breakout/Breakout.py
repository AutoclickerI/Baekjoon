n,x,m,*l=map(int,open(0).read().split())
print(min(v:=sum(i<x for i in l),m-v))