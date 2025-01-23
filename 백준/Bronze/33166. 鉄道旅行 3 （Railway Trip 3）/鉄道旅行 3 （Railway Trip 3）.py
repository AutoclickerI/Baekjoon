p,q,a,b=map(int,open(0).read().split())
print([q*a,p*a+(q-p)*b][p<q])