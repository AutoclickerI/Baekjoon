n,l=open(0)
p,q=map(l.split().count,'01')
print(p*int(n)+p*~p//2+p*q)