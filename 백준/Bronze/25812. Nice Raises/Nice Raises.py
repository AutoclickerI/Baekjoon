p,q,*l=map(int,open(0).read().split())
P=sum(i>q for i in l)
Q=sum(i<q for i in l)
print('012'[(P<Q)-(P>Q)])