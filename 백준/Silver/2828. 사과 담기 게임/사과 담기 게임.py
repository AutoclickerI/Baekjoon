N,M,J,*l=map(int,open(0).read().split())
p=0
print(sum(abs(p-(p:=min(i-1,max(p,i-M))))for i in l))