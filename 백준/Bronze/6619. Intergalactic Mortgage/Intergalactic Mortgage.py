for i in[*open(0)][:-1]:
    *l,r=i.split();X,Y,N=map(int,l);r=float(r)/1200
    if r<1e-9:a='YNEOS'[X>N*12*Y::2]
    else:a='YNEOS'[X*r>Y*(1-1/pow(1+r,12*N))::2]
    print(a)