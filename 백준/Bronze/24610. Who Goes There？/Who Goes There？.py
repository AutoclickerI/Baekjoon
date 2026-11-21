n,m,*l=map(int,open(0).read().split())
A=[i:=0]*m
while n*sum(l):t=l[i]>0;A[i]+=t;l[i]-=t;n-=t;i=-~i%m
print(*A)