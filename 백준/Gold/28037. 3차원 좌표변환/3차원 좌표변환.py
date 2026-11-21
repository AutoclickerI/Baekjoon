from cmath import*
for _ in[0]*int(input()):
    z,s=input().split()
    p,q,r=map(eval,input().split())
    if z=='2':
        p=rect(p,q)
        p,q=p.real,p.imag
    if z=='3':
        p,q,r=p*sin(q)*cos(r),p*sin(r)*sin(q),p*cos(q)
        p=p.real
        q=q.real
        r=r.real
    if s=='1':
        print(p,q,r)
    elif s=='2':
        p,q=polar(p+1j*q)
        print(p,q%(2*pi),r)
    else:
        a,b=polar(p+1j*q)
        l=(p*p+q*q+r*r)**.5
        if l:
            print(l.real,acos(r/l).real%(2*pi),b%(2*pi))
        else:
            print(0,0,0)