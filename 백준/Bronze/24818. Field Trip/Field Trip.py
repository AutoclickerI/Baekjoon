n,*l=map(int,open(0).read().split())
for i in range(1,n):l[i]+=l[i-1]
v=l[-1]//3
if l[-1]%3<1 and{v,v*2}&{*l}:print(l.index(v)+1,l.index(v*2)+1)
else:print(-1)