[N,s,e],*l=[map(int,i.split())for i in open(0)]
edges=[[]for _ in[0]*-~N]
for p,q,v in l:
    edges[p]+=(q,v),
    edges[q]+=(p,v),
vi=[0]*-~N
l=[(s,0,0)]
for s,c,w in l:
    if s==e:
        print(w-c)
        break
    for n,v in edges[s]:
        if vi[n]<1:
            vi[n]=1
            l+=(n,max(v,c),w+v),