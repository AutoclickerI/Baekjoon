N,M=map(int,input().split())
*l,=range(1,N+1)
a=0
for i in map(int,input().split()):
    p=l.index(i)
    if p==0:
        l.pop(0)
    else:
        a+=min(len(l)-p,p)
        l=l[p+1:]+l[:p]
print(a)