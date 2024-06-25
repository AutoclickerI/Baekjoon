from decimal import*
getcontext().prec=999
a,b,c,d,e=input().split()
b=Decimal(b)
e=Decimal(e)
d=Decimal(d)

if b*d==e:
    print('Whatever')
elif b*d>e:
    print('Power up, Evolve')
else:
    print('Evolve, Power up')