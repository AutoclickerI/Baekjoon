N,M,J,*l=map(int,open(p:=0).read().split())
print(sum(abs(p-(p:=min(i-1,max(p,i-M))))for i in l))