N=int(input())
p,q,r,s,*l=map(int,input().split())
for _ in[0]*N:
    v=[(p,q)]
    for _ in[0]*int(input()):
        v+=[*map(int,input().split())],
    v+=(r,s),
    l+=v,
def reduce(v):
    a=0
    for(i,j),(k,l)in zip(v,v[1:]):
        a+=abs(i-k)+abs(j-l)
    return a
print(min(range(N),key=lambda i:reduce(l[i]))+1)