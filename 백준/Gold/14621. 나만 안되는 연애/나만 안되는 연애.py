N,M=map(int,input().split())
l=input().split()
edges=[]
for _ in[0]*M:
    s,e,c=map(int,input().split())
    if l[s-1]!=l[e-1]:
        edges+=(c,s-1,e-1),
edges.sort()

*p,=range(N)

def find(n):
    if p[n]!=n:
        p[n]=find(p[n])
    return p[n]

r=0
for c,s,e in edges:
    s,e=sorted(map(find,[s,e]))
    if s!=e:
        r+=c
        p[e]=s
for i in range(N):
    p[i]=find(p[i])
print(-(0<max(p))or r)