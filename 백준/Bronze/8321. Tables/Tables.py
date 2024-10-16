n,k,s,*l=map(int,open(0).read().split())
l.sort()
c=k*s
for i in range(n):c-=l[~i];c<1<exit(print(i+1))