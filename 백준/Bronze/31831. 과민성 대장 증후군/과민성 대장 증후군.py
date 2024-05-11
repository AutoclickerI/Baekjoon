N,M,*l=map(int,open(t:=0).read().split())
print(sum(M<=(t:=max(t+i,0))for i in l))