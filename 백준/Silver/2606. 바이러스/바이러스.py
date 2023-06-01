N=int(input())
l=[*range(N+1)]
def union(n):
    if n-l[n]:l[n]=union(l[n])
    return l[n]

for _ in[0]*int(input()):
    p,q=map(int,input().split())
    p,q=sorted([union(p),union(q)])
    l[q]=l[p]
for i in range(N+1):union(i)
print(l.count(1)-1)