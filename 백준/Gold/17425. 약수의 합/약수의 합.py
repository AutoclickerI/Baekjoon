f=[0]*1000000
for i in range(1,1000001):
    for j in range(i,1000001,i):
        f[j-1]+=i

g=[0]
for i in f:g+=g[-1]+i,

for i in[*open(0)][1:]:print(g[int(i)])