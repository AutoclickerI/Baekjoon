_,*l=[[*map(int,i.split()[1:])]for i in open(0)]
f=lambda p,q:p(map(q,l))
print(f(max,max),f(min,min),f(max,sum),f(min,sum))