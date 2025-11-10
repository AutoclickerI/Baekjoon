N,M,*v=map(int,open(0).read().split())
s,e=max(v)-1,10**9
while-~s<e:
 x=s+e>>1;c=z=0
 for i in v:z=[z,x][f:=z<i]-i;c+=f
 if M<c:s=x
 else:e=x
print(e)