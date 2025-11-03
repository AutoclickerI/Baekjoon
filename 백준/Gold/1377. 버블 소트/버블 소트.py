N,*l=map(int,open(0))
print(max(map(int.__sub__,sorted(R:=range(N),key=l.__getitem__),R))+1)