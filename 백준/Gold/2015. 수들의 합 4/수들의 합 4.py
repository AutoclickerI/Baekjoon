N,K,*A=map(int,open(0).read().split())
s=[r:=0]
for i in A:s+=s[-1]+i,
d={}
for i in s:r+=d.get(i-K,0);d[i]=d.get(i,0)+1
print(r)