def inv(n):
    n+=1
    v=n//3
    return(-2*v+v*(v+1)//2*3)*3-2+n%3*v*3

for i in[*open(0)][1:]:
    s=0
    e=10**18+1
    while 1<e-s:
        m=s+e>>1
        if int(i)<inv(m):
            e=m
        else:
            s=m
    print(e-1)