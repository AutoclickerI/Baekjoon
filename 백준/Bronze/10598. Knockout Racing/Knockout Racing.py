(n,_),*l=[[*map(int,i.split())]for i in open(0)]
for x,y,t in l[n:]:print(sum(x<=a+min(t%(z:=b-a<<1),z-t%z)<=y for a,b in l[:n]))