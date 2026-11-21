for i in[*open(0)][1:]:
    s=1
    e=2**60
    while 1<e-s:
        m=s+e>>1
        v=m//3
        if(m%3-2)*v*3-v*~v//2*9-2>int(i):e=m
        else:s=m
    print(s-1)