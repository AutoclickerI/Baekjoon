[W,H],_,*l=[map(int,i.split())for i in open(0)]
v=[[0,H],[0,W]]
for q,n in l:v[q]+=n,
for i in v:i.sort()
print(max((j-i)*(l-k)for i,j in zip(v[0],v[0][1:])for k,l in zip(v[1],v[1][1:])))