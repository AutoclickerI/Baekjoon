from decimal import*
getcontext().prec=99
for i in[*open(0)][1:]:a,b,c,d=map(Decimal,i.split());p,q=round(a+b.sqrt(),50),round(c+d.sqrt(),50);print(['Equal','Greater','Less'][(p>q)-(p<q)])