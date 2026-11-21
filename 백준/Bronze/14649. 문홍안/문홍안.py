p,*l=open(0).read().split()
for v in 0,1,2:print(f'{int(p)/100*sum(v==sum([a<i,i<a][b<'R']for a,b in zip(map(int,l[1::2]),l[2::2]))%3for i in range(1,101)):.2f}')