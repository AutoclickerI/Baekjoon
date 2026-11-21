next(l:=open(0))
for i,j in zip(l,l):print('YNEOS'[all(i[k//5*2]!=j[k%5*2]for k in range(25)if k//5-k%5)::2])