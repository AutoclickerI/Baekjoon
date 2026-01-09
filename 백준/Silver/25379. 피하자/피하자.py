n,s=open(r:=0)
v=0
for i in s.split():v+=(r:=r+(f:=int(i)&1))-r*f
print(min(v,(int(n)-r)*r-v))