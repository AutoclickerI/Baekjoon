N,M,*l=map(int,open(a:=0).read().split())
for i in range(1,N):
 if abs(l[i-1]-l[i])<M:l[i]=1e18;a+=1
print(a)