N,*l=map(int,open(0).read().split())
l.sort()
mv=float('inf')
for s in range(N):
    for e in range(s+3,N):
        v=l[s]+l[e]
        p1=s+1
        p2=e-1
        while p1<p2:
            mv=min(mv,abs(v-l[p1]-l[p2]))
            if 0<v-l[p1]-l[p2]:
                p1+=1
            else:
                p2-=1
print(mv)