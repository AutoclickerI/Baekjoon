from decimal import*
getcontext().prec=50
for i in range(int(input())):
    A,B,C,d=map(D:=Decimal,input().split())
    def f(x):
        return A*x**3+B*x**2+C*x+d
    def find(s,e):
        while e-s>10**-10:
            p=(s+e)/2
            if f(p)*f(s)>0:
                s=p
            else:
                e=p
        return s
    if B**2-3*A*C<0:
        ans=[find(D(-1000000),D(1000000))]
    else:
        sol=sorted([(-B-(B**2-3*A*C)**D('0.5'))/(3*A),(-B+(B**2-3*A*C)**D('0.5'))/(3*A)])
        if round(f(sol[0])*f(sol[1]),11)>0:
            ans=[find(D(-1000000),D(1000000))]
        elif round(f(sol[0]),11)==0 or round(f(sol[1]),11)==0:
            if round(f(sol[0]),11)==0:
                if round(sol[0],11)==round(sol[1],11):
                    ans=[sol[0]]
                else:
                    ans=[sol[0],find(sol[1],D(1000000))]
            else:
                ans=[find(D(-1000000),sol[0]),sol[1]]
        else:
            ans=[find(D(-1000000),sol[0]),find(sol[0],sol[1]),find(sol[1],D(1000000))]
    ans=['{:.10f}'.format(i) for i in ans]
    print(*ans)