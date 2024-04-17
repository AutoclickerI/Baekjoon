N,M,T,*l=map(int,open(0).read().split())
print(l[0]-M+max(0,T-l[-1]-M)+sum(max(0,j-i-2*M)for i,j in zip(l,l[1:])))