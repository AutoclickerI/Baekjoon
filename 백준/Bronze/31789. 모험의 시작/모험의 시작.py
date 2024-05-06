_,[p,q],*r=[map(int,i.split())for i in open(0)]
print('YNEOS'[all(j>p*(k>q)for j,k in r)::2])