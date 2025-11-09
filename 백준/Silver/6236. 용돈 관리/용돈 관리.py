N,M,*l=map(int,open(0).read().split())

def check(K):
    c=m=0
    for i in l:
        if m<i:
            m=K
            c+=1
        if m<i:
            return 0
        m-=i
    return c<=M

s=0
e=10**10
while 1<e-s:
    m=s+e>>1
    if check(m):
        e=m
    else:
        s=m
print(e)