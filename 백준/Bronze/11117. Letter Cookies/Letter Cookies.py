_,*l=open(0)
while l:
 n=int(l[1])
 for i in l[2:n+2]:print('YNEOS'[any(l[0].count(c)<i.count(c)for c in i)::2])
 l=l[n+2:]