_,*l=map(int,open(0).read().split())
while l:
 M,N,*l=l;z=l[:M*N];l=l[M*N:]
 for i in range(M,M*N):z[i%M]*=z[i]
 print(max((z[i],i+1)for i in range(M))[1])