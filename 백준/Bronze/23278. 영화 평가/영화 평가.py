N,L,H,*l=map(int,open(0).read().split())
print(sum(sorted(l)[L:N-H])/(N-L-H))