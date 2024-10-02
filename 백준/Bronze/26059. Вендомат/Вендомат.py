(n,p,q),*l=[i.replace(*', ').split()for i in open(0)]
r=c=-1
for s,x,y in l:
    x,y=int(x),int(y)
    if int(p)>=x and int(q)>=y>c-x*100:r,c=s,x*100+y
print(r)