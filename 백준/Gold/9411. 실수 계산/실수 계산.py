from decimal import*
getcontext().prec=30
for d in[0]*int(input()):
 N=0
 while d!='0':N+=Decimal(d:=input())
 print(f'{N.normalize():f}')