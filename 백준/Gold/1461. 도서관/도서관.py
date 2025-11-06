N,M,*l=map(int,open(0).read().split())
l.sort()
print(2*sum(max(l[~i],0)-min(l[i],0)for i in range(0,N,M))-max(-l[0],l[-1]))