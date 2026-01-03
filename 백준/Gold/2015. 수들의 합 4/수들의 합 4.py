N,K,*A=map(int,open(0).read().split())
s=r=0
d={0:1}
for i in A:s+=i;r+=d.get(s-K,0);d[s]=d.get(s,0)+1
print(r)