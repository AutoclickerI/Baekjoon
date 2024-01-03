from decimal import*
getcontext().prec=999
n=sum(map(ord,s:=input()))
print(chr(max(round(Decimal(n)/len(s)-Decimal('1e-100')),ord(max(s))-1,65)))