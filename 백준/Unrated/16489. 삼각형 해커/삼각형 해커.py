from decimal import*
getcontext().prec=99
a,b,c=map(D:=Decimal,input().split())
s=(a+b+c)/2
S=(s*(s-a)*(s-b)*(s-c)).sqrt()
print(S,a*b*c/(4*S),2*S/(a+b+c),max(D(0),(a*b*c/(4*S)*(a*b*c/(4*S)-(4*S/(a+b+c))))).sqrt(),a*b*c/(4*S)+2*S/(a+b+c),sep='\n')