_,*l=map(int,open(0).read().split())
while l:
 M,N,*l=l
 for i in range(M,M*N):l[i%M]*=l[i]
 print(max((l[i],i+1)for i in range(M))[1]);l=l[M*N:]