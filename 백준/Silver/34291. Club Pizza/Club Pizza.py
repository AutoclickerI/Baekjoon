n,c,*l=map(int,open(0).read().split())
v=[1e9]*25+[0]
R=range(26)
for i in sorted({*l[::2]}):
 for j in R:v[j]=min(v[j],v[j-25]+min(l[2*k+1]for k in range(n)if l[2*k]==i))
for i in R:c<v[~i]<exit(print(i-1))