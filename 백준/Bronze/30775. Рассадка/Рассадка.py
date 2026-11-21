M,_,*l=map(int,open(0).read().split())
s=sum(l)
print(s//M+(s%M>0))