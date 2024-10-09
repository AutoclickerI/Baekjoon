(_,m),*l=[map(int,i.split())for i in open(0)]
d={}
a=0
for t,x in l:
    if t<2:a+=d.get(-x%m,0);d[x%m]=d.get(x%m,0)+1
    else:d[x%m]=d.get(x%m,0)-1;a-=d.get(-x%m,0)
    print(a)