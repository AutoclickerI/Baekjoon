[N,M],*b=[[*map(int,i.split())]for i in open(0)]
c=[0]*M
for i in b:
    t=[c[0]+i[0]]
    for v in range(1,M):
        t+=max(t[-1],c[v])+i[v],
    c=t
print(c[-1])