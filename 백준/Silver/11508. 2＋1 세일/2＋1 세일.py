_,*l=map(int,open(0))
l.sort()
del l[-3::-3]
print(sum(l))