N=int(input())
d={}
for _ in[0]*N:
    s,e,c=input().split()
    d[s]=d.get(s,[])
    d[e]=d.get(e,[])
    se=[e,int(c)]
    es=[s,int(c),se]
    se+=es,
    d[s]+=se,
    d[e]+=es,

from heapq import*
res=0
while 1:
    v={'A':float('inf')}
    p={}
    hq=[(-float('inf'),'A')]
    while hq:
        x,n=heappop(hq)
        if-x<v[n]:continue
        for e,c,se in d[n]:
            nc=min(-x,c)
            if v.get(e,0)<nc:
                v[e]=nc
                p[e]=se
                heappush(hq,(-nc,e))
    if 'Z'not in v:
        break
    i='Z'
    flow=v['Z']
    res+=flow
    while i!='A':
        p[i][2][1]-=flow
        p[i][1]-=flow
        i=p[i][0]
print(res)