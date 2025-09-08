n,*d=map(int,open(0))
u=n*3//10+1>>1
print(int(sum(sorted(d)[u:n-u])/(n-u*2or 1)+.5))