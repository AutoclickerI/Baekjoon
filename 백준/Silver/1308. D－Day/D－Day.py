from datetime import*
y,m,d,*l=map(int,open(0).read().split())
print(['gg',f'D-{(date(*l)-date(y,m,d)).days}'][l<[y+1e3,m,d]])