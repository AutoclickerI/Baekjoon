r=0
z=[]
for _ in[0]*int(input()):
    s=e=1
    N=int(input())
    v,*l=map(int,input().split())
    m=v
    x=s,e
    ll=e-s
    for i in l:
        e+=1
        if v<=0:
            s=e
            v=0
        v+=i
        if m<v or m==v and e-s<ll:
            m=v
            x=s,e
            ll=e-s
    r+=m
    z+=x,
print(r)
for i in z:print(*i)