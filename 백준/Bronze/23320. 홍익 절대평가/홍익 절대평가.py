N,*l,X,Y=map(int,open(0).read().split())
print(N*X//100,sum(i>=Y for i in l))