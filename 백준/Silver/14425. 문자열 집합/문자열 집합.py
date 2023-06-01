p,q,*l=open(0).read().split();p=int(p)
print(sum(i in l[:p] for i in l[p:]))