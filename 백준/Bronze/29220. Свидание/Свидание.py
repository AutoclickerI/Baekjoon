p,_,*l=map(int,open(0).read().split())
print('YNEOS'[sum(l)-min(l)<=p::2])