N,M,*l=map(int,open(0).read().split())
print(sum(l[::-2][:M])/N)