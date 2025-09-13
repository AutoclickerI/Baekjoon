d={}
(n,c),*l=[map(int,i.split())for i in open(0)]
for t,p in l:d[t]=min(d.get(t,p),p)
v=[1e9]*25+[0]
R=range(26)
for i in sorted(d):
 for j in R:v[j]=min(v[j],v[j-25]+d[i])
for i in R:c<v[~i]<exit(print(i-1))