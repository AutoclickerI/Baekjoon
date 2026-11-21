p,q,*r=map(int,open(0).read().split())
M=max(0,max(r)-q)
print(sum(max(0,i-M)for i in r))