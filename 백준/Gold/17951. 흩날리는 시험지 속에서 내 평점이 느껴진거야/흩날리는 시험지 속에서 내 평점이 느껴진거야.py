N,K,*x=map(int,open(0).read().split())

def chk(p):
    r=c=0
    for i in x:
        c+=i
        if p<=c:
            c=0
            r+=1
    return r

s=1
e=10**9
while 1<e-s:
    m=s+e>>1
    if K<=chk(m):
        s=m
    else:
        e=m
print(s)