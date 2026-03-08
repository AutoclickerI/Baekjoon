N,k=map(int,input().split())
s=[input(),input()]

v=[2*[float('inf')]for _ in[0]*N]

v[0][0]=0

from heapq import*
hq=[(0,0,0)]

while hq:
    c,f,p=heappop(hq)
    for dp,df in(-1,0),(1,0),(k,1):
        np,nf=p+dp,f^df
        if N<=np:
            exit(print(1))
        if 0<=np and s[nf][np]=='1'and c<np and c+1<v[np][nf]:
            v[np][nf]=c+1
            heappush(hq,(c+1,nf,np))
print(0)