n,*l=open(0).read().split()
p,q=map(l.count,'01')
print(p*int(n)+p*~p//2+p*q)