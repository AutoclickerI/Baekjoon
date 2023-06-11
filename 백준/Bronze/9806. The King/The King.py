_,q,*l=map(int,open(0).read().split())
print(sum(i**q for i in l if i**q>0))