N,K,*l=map(int,open(0).read().split())
l.sort()
print(sum(sorted(map(int.__sub__,l[1:],l))[:N-K]))