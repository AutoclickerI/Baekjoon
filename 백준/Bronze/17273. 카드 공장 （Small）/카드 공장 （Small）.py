l=open(0).read().split()
f=2
for i in l:f^=int(l[f])<=int(i)
print(l[f])