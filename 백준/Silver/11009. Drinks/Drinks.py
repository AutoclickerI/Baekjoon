F=__import__('fractions').Fraction
for i in[*open(0)][1:]:
    p,q=map(int,i.split())
    a=F(p,q+p)
    f=1-a
    while q>0:
        f*=F(q:=q-1,q+p)
        q-=1
        if~q:a+=f*F(p,q+p);f*=F(q,q+p)
    print(a)