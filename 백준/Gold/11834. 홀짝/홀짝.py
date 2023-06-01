from decimal import*
getcontext().prec=100
n=Decimal(input())*2
N=int(n**Decimal('0.5'))
if n>N*(N+1):N+=1
if n<=N*(N-1):N-=1
print(n-1+1-N)  