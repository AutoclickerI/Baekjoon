n,*l=map(int,open(0).read().split())
s=sum(~i%2for i in l)
print(+(s==n//2))