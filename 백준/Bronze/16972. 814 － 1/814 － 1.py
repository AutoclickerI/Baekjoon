N=16280

def trifill(v):
    l=[]
    f=1
    y=0
    dy=int(3**.5/2*v)
    sx=v//2
    while y<=N:
        if f:
            x=sx
            while x<=N:
                l+=(x,y),
                x+=v
        else:
            x=0
            while x<=N:
                l+=(x,y),
                x+=v
        y+=dy
        f^=1
    return l

*z,(p,q)=trifill(625)[:814]
for x,y in z:print(x-8140,y-8140)
print(p-8140,q-8141)