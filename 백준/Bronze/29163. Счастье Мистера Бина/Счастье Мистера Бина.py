n,*l=map(int,open(0).read().split())
print(['Sad','Happy'][sum(i%2for i in l)*2<n])