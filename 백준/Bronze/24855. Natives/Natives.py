n,*l=map(int,open(0).read().split())
print(sum(sorted(l)[0-n//2:]))