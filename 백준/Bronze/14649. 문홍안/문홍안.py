p,*A=open(0).read().split()
for b in map([sum([a<i,i<a][b<'R']for a,b in zip(map(int,A[1::2]),A[2::2]))%3for i in range(1,101)].count,range(3)):print(f'{int(p)/100*b:.2f}')