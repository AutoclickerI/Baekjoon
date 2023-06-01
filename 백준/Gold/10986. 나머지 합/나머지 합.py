N,M,*l=map(int,open(0).read().split())
l+=[0]
d={0:1}
for i in range(N):l[i]=(l[i]+l[i-1])%M;d[l[i]]=d.get(l[i],0)+1
N=0
for i in d:N+=d[i]*(d[i]-1)//2
print(N)