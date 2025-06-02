for i in[*open(0)][1:]:
    s=1
    e=2**60
    while 1<e-s:
        m=s+e>>1
        v=m//3
        if int(i)<-6*v+v*(v+1)//2*9-2+m%3*v*3:e=m
        else:s=m
    print(s-1)