N,_,*l=map(int,open(0).read().split())
print(*sorted({*range(1,N+1)}-{*l})or'*')