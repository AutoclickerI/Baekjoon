p,*l=map(int,open(0).read().split())
l.sort()
while p:l[-p]*=p;p-=1
print(sum(l))