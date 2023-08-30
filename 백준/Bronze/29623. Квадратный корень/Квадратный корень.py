from decimal import*
getcontext().prec=200
for _ in[0]*int(input()):
    a,b,c,d=map(D:=Decimal,input().split())
    p,q=a+b.sqrt(),c+d.sqrt()
    if round(p,100)==round(q,100):
        print('Equal')
    elif p>q:
        print('Greater')
    else:
        print('Less')