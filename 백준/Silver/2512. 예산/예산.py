N,*l,M=map(int,open(0).read().split())
M-=sum(l)
*l,v=0,*sorted(l)
c=1
while M<0:
 t=l.pop()-v
 if t*c<M:M//=c;v+=M;M=0
 else:M-=t*c;c+=1;v+=t
print(v)