from decimal import*
getcontext().prec=999
p,q,r,s=map(Decimal,input().split())
print(int((min(p,q)+min(r,s)).sqrt()))