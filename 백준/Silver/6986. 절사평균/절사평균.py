from decimal import*
N,K,*l=map(int,open(0).read().replace('.','').split())
l.sort()
l[:K]=[l[K]]*K
if K:l[-K:]=[l[~K]]*K
print(f'{sum(l[K:-K]or l)/Decimal(10*N-20*K)+Decimal("0.00000001"):.2f} {sum(l)/Decimal(10*N)+Decimal("0.00000001"):.2f}')