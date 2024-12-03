N,*l=map(int,open(0).read().replace('.','').split())
print(sum(max(i*k//10-j,i-j*k//10)for i,j,k in zip(l,l[N:],l[2*N:])))