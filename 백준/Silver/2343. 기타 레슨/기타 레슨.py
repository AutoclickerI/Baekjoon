N,M,*l=map(int,open(0).read().split())

s=0
e=10**9

def count():
    c=1
    v=0
    for i in l:
        if v+i<=m:
            v+=i
        else:
            if m<i:return 1e18
            v=i
            c+=1
    return c

while s+1<e:
    m=s+e>>1
    if M<count():
        s=m
    else:
        e=m

print(e)