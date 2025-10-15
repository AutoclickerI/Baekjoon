N,*l=map(int,open(0).read().split())
l=[N-i for i in l]
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
            print(*[N-i for i in l],N-v,*[N-i for i in sorted(t)])
            break