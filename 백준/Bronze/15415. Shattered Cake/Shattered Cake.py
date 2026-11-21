w,_,*l=map(int,open(0).read().split())
print(sum(p*q for p,q in zip(l[::2],l[1::2]))//w)