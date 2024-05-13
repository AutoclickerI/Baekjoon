N,M,*l=map(int,open(t:=0).read().split())
print(sum(M<=(t:=(t>0)*t+i)for i in l))