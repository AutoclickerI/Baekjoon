n,s,*l=map(int,open(0).read().split())
for v,d in zip(l,l[n:]):s+=d;print(end='MVT'[(v<s)-(v>s)])