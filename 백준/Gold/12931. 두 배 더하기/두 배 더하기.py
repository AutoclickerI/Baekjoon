N,*l=map(int,open(0).read().split())
c=0
while any(l):
    c+=sum(i%2 for i in l)
    l=[i&-2 for i in l]
    c+=any(l)
    l=[i>>1 for i in l]
print(c)