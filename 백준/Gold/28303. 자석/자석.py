N,K,*l=map(int,open(0).read().split())
R=range(N)
m,*l1=(l[i]-K*i for i in R)
z,*l2=(l[~i]-K*i for i in R)
M=l1[0]-m
Z=l2[0]-z
for i,j in zip(l1,l2):M=max(i-m,M);m=min(i,m);Z=max(j-z,Z);z=min(j,z)
print(max(M,Z))