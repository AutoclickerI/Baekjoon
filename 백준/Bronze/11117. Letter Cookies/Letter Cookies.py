_,*l=open(0)
while l:s,n,*l=l;exec("i=l.pop(0);print('YNEOS'[any(s.count(c)<i.count(c)for c in i)::2]);"*int(n))