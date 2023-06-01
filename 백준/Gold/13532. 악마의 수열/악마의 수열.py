from decimal import*
getcontext().prec=100000
D=Decimal
i=int(input())
x=str((2**i-(-1)**i)//3/D(2**(i-1)))[2:]
t=0
while x[t]=='6':
    t+=1
print(t)