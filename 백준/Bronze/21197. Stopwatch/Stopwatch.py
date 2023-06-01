n,*l=map(int,open(0))
print(n%2*'still running'or sum(l[1::2])-sum(l[::2]))