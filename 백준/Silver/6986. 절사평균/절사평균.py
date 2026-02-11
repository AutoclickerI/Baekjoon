N,K,*l=map(eval,open(0).read().split())
l.sort()
A=sum(l[K:N-K])+1e-8
print(f'{A/(N-2*K):.2f} {(l[K]*K+A+l[~K]*K)/N:.2f}')