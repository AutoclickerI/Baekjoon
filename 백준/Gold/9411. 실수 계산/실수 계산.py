from decimal import*
getcontext().prec=30
D=Decimal
for i in[0]*int(input()):
 d=N=D(0)
 while d!='0':N+=D(d:=input())
 print(f'{N.normalize():f}')