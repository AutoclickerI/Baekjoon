N,M=map(int,input().split())
b=[input()[::2]for _ in[0]*N]

h=[]
c=[]

for y in range(N):
    for x in range(N):
        if b[y][x]=='2':
            c+=(y,x),
        if b[y][x]=='1':
            h+=(y,x),

v=[]
for y,x in c:
    v+=[abs(y-i)+abs(j-x)for i,j in h],

from itertools import combinations

a=1e18

for idxs in combinations(v,M):
    a=min(a,sum(map(min,zip(*idxs))))

print(a)