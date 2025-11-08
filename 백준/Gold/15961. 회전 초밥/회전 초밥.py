N,d,k,c,*l=map(int,open(m:=0).read().split())
l*=2
v={}
for i in l[:k]:v[i]=v.get(i,0)+1

for i in range(k,2*N):
    v[l[i]]=v.get(l[i],0)+1
    v[l[i-k]]-=1
    if v[l[i-k]]<1:
        del v[l[i-k]]
    m=max(m,len(v)+(c not in v))
print(m)