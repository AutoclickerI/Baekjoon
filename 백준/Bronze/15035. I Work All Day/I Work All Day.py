_,*l,n=map(int,open(0).read().split())
print(min(l,key=lambda x:n%x))