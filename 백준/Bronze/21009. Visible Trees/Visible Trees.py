def f(l):
    t=l[0];r=1
    for a in l[1:]:r+=a>t;t=max(a,t)
    return r
l=[[*map(int,i.split())]for i in open(0)][1:]
print(*map(f,[*zip(*l)]+l))