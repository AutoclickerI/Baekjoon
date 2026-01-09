[N],*l=[map(int,i.split())for i in open(0)]

*p,=range(N+1)

def find(n):
    if p[n]!=n:
        p[n]=find(p[n])
    return p[n]

for s,e in l:
    s,e=sorted(map(find,[s,e]))
    p[e]=s

print(*{find(i+1)for i in range(N)})