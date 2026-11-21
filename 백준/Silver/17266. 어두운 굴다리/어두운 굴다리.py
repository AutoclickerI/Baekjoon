N,_,*l=map(int,open(0).read().split())
print(-min(*[i-j>>1for i,j in zip([-l[0]]+l,l)],l[-1]-N))