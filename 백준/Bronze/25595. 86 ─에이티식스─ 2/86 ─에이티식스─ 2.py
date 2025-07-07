n,*l=map(int,open(0).read().split())
i=l.index(2)
print('Kiriya'*any(i//n+i%n+j//n+j%n&1<l[j]&1for j in range(n*n))or'Lena')