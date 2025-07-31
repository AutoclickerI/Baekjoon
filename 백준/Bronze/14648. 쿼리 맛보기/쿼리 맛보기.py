_,a,*l=[map(int,i.split())for i in open(0)]
a=[0,*a]
for b,c,d,*e in l:
 r=sum(a[c:d+1])
 if b-1:r-=sum(a[e[0]:e[1]+1])
 else:a[c],a[d]=a[d],a[c]
 print(r)