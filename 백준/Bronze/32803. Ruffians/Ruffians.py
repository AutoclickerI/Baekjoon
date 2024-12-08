next(l:=open(0))
r=range(5)
for i,j in zip(l,l):print('YNEOS'[all(i[a*2]!=j[b*2]for a in r for b in r if a-b)::2])