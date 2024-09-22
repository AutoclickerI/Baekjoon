N,Q,*l=map(int,open(0).read().split())
while l[N:]:print(sum(l[l[N]-1:l[N+1]]));N+=2