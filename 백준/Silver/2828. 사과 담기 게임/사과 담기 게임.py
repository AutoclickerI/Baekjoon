N,M,J,*l=map(int,open(r:=0).read().split())
p=1
for i in l:i=min(i,max(p,i-M+1));r+=abs(p-i);p=i
print(r)