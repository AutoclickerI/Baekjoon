from decimal import*
getcontext().prec=99
H=G=Decimal(0)
for i in input():G+=i in'SAD';H+=i in'HAPY'
if H+G:
    print(f'{100*H/(H+G)+Decimal("1e-50"):.2f}')
else:
    print('50.00')