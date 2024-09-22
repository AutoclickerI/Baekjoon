N,Q,*l=map(int,open(0).read().split())
z=l[N:]
while z:s,e,*z=z;print(sum(l[s-1:e]))