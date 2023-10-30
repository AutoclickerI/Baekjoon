p,q,*l=map(int,open(0).read().split())
if all(i<p for i in l):
    print(-1)
else:
    print(1+sum(min(i,p-1)for i in l))