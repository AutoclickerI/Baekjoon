[N],*l=[[*map(int,i.split())]for i in open(0)]
(p,q),(r,s)=min(l[:N]),min(l[N:])
print(r-p,s-q)