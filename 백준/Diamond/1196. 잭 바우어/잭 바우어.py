from decimal import*
getcontext().prec=99
N,K=map(D:=Decimal,input().split())
H=lambda n:sum(1/D(i+1)for i in range(int(n)))if n<1e6 else n.ln()+D('0.57721566490153286')+(6*n-1)/n/n/12
print(N*(H(N)-H(N-K)))