n,a,b,c=map(int,open(0).read().split())
print((('AB'*a)[:a]+('ab'*b)[:b]+'01'*n)[:n])