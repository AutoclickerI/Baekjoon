N,K,*l=open(0).read().split()
K=int(K)+1
N=int(N)
v=[0]*22
*l,=map(len,l)
r=0
for i in l[:K]:r+=v[i];v[i]+=1
for i in range(N-K):
    v[l[i]]-=1
    r+=v[l[i+K]]
    v[l[i+K]]+=1
print(r)