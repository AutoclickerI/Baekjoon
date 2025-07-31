_,a,*l=[[*map(int,i.split())]for i in open(0)]
for b,c,d,*e in l:
 r=sum(a[c-1:d])
 if b-1:r-=sum(a[e[0]-1:e[1]])
 else:a[c-1],a[d-1]=a[d-1],a[c-1]
 print(r)