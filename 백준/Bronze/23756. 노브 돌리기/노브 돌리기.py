_,*l=map(int,open(0))
print(sum(min(x:=abs(s-t),360-x)for s,t in zip(l,l[1:])))