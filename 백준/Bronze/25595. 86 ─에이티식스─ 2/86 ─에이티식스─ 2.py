n,*l=map(int,open(0).read().split())
i=l.index(2)
print('KLierniay a'[all(~l[j]%2+(i//n+i%n^j//n+j%n)%2for j in range(n*n))::2])