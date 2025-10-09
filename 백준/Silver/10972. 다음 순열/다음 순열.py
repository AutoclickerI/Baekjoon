*l,=map(int,[*open(0)][1].split())
if l[::-1]==sorted(l):
    print(-1)
else:
    t=[]
    for i in range(len(l)):
        t+=l.pop(),
        if l[-1]<max(t):
            v=min(n for n in t if l[-1]<n)
            t+=l.pop(),
            t.remove(v)
            print(*l,v,*sorted(t))
            break