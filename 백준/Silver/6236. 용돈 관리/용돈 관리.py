N,M,*v=map(int,open(0).read().split())
s,e=max(v)-1,10**9
while 1<e-s:
 x=s+e>>1;c=z=0
 for i in v:f=z<i;z=(x*f or z)-i;c+=f
 if M<c:s=x
 else:e=x
print(e)