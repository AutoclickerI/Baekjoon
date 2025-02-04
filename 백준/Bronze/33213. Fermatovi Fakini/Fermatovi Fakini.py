n,*l=map(int,open(0).read().split())
v=sum(i%2for i in l)*2<n
while-~v in l:v+=2
print(-~v)