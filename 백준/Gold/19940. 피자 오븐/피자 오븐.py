v=[float('inf')]*61
v[0]=0
t=[[0]*5]*61

from heapq import*

hq=[(0,0,[0]*5)]

while hq:
    c,n,l=heappop(hq)
    if v[n]<c:
        continue
    for dn,i in(-1,4),(1,3),(-10,2),(10,1),(60,0):
        nn=n+dn
        if 0<nn<61 and c+1<v[nn]:
            v[nn]=c+1
            t[nn]=l[:]
            t[nn][i]+=1
            heappush(hq,(c+1,nn,t[nn]))

for i in[*open(0)][1:]:
    i=int(i)
    r=t[i%60][:]
    r[0]+=i//60
    print(*r)