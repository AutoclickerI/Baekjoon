_,*l=map(str.split,open(0))
I=int
print('yneos'[any(I(i)>I(k)or I(j)>I(l)for(i,j),(k,l)in zip(l,l[1:]))::2])