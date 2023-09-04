for i in[*open(0)][:-1]:
    p,q,r,s=map(int,i.split())
    if p==0:
        print(s//r//q,q,r,s)
    if q==0:
        print(p,s//p//r,r,s)
    if r==0:
        print(p,q,s//p//q,s)
    if s==0:
        print(p,q,r,p*q*r)