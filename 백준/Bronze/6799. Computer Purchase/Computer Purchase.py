def f(i):n,*l=i.split();r,s,d=map(int,l);return-2*r-3*s-d,n
for*_,i in sorted(map(f,[*open(0)][1:]))[:2]:print(i)