from decimal import*
getcontext().prec=99
for i in[*open(0)][1:]:
    a,b,c,d=map(Decimal,i.split())
    if round(p:=a+b.sqrt(),50)==round(q:=c+d.sqrt(),50):print('Equal')
    elif p>q:print('Greater')
    else:print('Less')