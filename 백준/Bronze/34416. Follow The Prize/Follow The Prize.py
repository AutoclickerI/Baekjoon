_,p,_,*q=open(0)
p={p[:-1]}
for i in q:p=max(p,{*i.split()})-p or p
print(*p)