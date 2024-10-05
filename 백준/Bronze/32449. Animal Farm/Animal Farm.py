a,b=x=[[],[]]
for i in[*open(0)][1:]:i,j=i.split();x[i=='pig']+=int(j),
m=max(b)
print(m+sum(i*(i<m)for i in a))