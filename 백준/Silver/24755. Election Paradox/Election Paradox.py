N,*l=map(int,open(0).read().split())
print(sum(l+[~i//2for i in sorted(l)[:N//2+1]]))