N,*l=map(int,open(v:=0).read().split())
K=sum(l)//N
s=[v:=v+i-K for i in l]
print(sum(s[:N])-min(s)*N)