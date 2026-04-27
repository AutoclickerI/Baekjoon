def find(n):
    if n!=p[n]:
        p[n]=find(p[n])
    return p[n]

def mst(t):
    c=r=0
    for w,s,e in sorted(edges,key=lambda i:i[0]!=t):
        s=find(s)
        e=find(e)
        if s-e:
            p[e]=s
            c+=w=='B'
            r+=1
    return c

while 1:
    N,M,K=map(int,input().split())
    if N<1:break
    edges=[]
    for _ in[0]*M:
        w,s,e=input().split()
        edges+=(w,int(s),int(e)),
    
    *p,=range(N+1)
    a=mst('R')
    *p,=range(N+1)
    b=mst('B')
    print(+(a<=K<=b))