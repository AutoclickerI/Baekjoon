[n],*l,_=[map(int,i.split())for i in open(0)]

v=[n*[9e9]for _ in[0]*n]
for s,e in l:
    v[s-1][e-1]=v[e-1][s-1]=1
for i in range(n):
    v[i][i]=0

for m in range(n):
    for s in range(n):
        for e in range(n):
            v[s][e]=min(v[s][e],v[s][m]+v[m][e])

a=[max(i)for i in v]

m=min(a)
arr=[i+1 for i in range(n)if a[i]==m]
print(m,len(arr),*arr)