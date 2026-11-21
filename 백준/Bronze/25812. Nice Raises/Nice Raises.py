p,q,*l=map(int,open(0).read().split())
s=sum((i>q)-(i<q)for i in l)
print(s and(s>0)+1)