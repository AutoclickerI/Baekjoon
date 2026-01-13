N,M,*l=map(int,open(0).read().split())

s=-1
e=9**9

def check(m):
    c=1
    Mv=0
    mv=1e9
    for i in l:
        if m<i-mv or m<Mv-i:
            c+=1
            Mv=0
            mv=1e9
        Mv=max(Mv,i)
        mv=min(mv,i)
    return c

while 1<e-s:
    m=s+e>>1
    if M<check(m):
        s=m
    else:
        e=m
print(e)