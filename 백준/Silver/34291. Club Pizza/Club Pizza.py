d={}
(n,c),*l=[map(int,i.split())for i in open(0)]
for t,p in l:d[t]=min(d.get(t,p),p)
v=[1e9]*26
v[0]=0
for i in sorted(d):
    for j in range(25,0,-1):
        v[j]=min(v[j],v[j-1]+d[i])
for i in range(26):
    if c<v[i]:exit(print(i-1))