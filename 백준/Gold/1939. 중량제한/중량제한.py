[N,M],*l,[s,e]=[map(int,i.split())for i in open(0)]

edges=[[]for _ in[0]*-~N]

for a,b,c in l:
    edges[a]+=(-c,b),
    edges[b]+=(-c,a),

for i in edges:i.sort()

v=[0]*-~N
v[s]=float('inf')

l=[(s,v[s])]

for i,c_n in l:
    if c_n<v[i]:continue
    for c,n in edges[i]:
        if v[n]<min(v[i],-c):
            v[n]=min(v[i],-c)
            l+=(n,min(v[i],-c)),

print(v[e])