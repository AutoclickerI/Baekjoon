M,_,*l=map(int,open(0).read().split())
print(sum(l)//M+(sum(l)%M>0))