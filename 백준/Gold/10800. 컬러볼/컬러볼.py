[N],*l=[[*map(int,i.split())]for i in open(0)]

b=[[]for _ in[0]*N]
g=[]

for c,v in l:b[c-1]+=v,;g+=v,

bs=[]
for i in b:
    i.sort()
    t=[0]
    for v in i:t+=t[-1]+v,
    bs+=t,

g.sort()
gs=[0]
for i in g:
    gs+=gs[-1]+i,

from bisect import*

for c,v in l:
    print(gs[bisect_left(g,v)]-bs[c-1][bisect_left(b[c-1],v)])