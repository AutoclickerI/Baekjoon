n,*d=map(int,open(0))
u=int(n*.15+.5)
print(int(sum(sorted(d)[u:n-u])/(n-u*2or 1)+.5))