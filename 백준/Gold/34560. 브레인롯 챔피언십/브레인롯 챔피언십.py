_,*l=map(str.split,open(0))

edges=[[]for _ in[0]*len(l)]
deg=[0]*len(l)

for i in range(len(l)):
    p1,a1,s1=map(int,l[i][1:])
    for j in range(i+1,len(l)):
        p2,a2,s2=map(int,l[j][1:])
        f1=(p2<p1)+(a2<a1)+(s2<s1)
        f2=(p1<p2)+(a1<a2)+(s1<s2)
        if f1<f2:
            edges[j]+=i,
            deg[i]+=1
        if f2<f1:
            edges[i]+=j,
            deg[j]+=1

nodes=[i for i in range(len(l))if deg[i]<1]
v=nodes[:]

for i in v:
    for e in edges[i]:
        deg[e]-=1
        if deg[e]<1:
            v+=e,
if any(deg):
    print('Paradoxe Absurdo')
else:
    for i in sorted(l[i][0]for i in nodes):
        print(i)