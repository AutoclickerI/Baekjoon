from decimal import*
getcontext().prec=99
N,K=map(D:=Decimal,input().split())
H=lambda n:sum(N/D(i+1)for i in range(int(n)))if n<1e6else(n.ln()+D(.577215665)+(6-1/n)/n/12)*N
print(H(N)-H(N-K))