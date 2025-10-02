_,*l=map(int,open(0))
l.sort()
v=0
while 1<len(l) and 1<l[-2]:
    v+=l.pop()*l.pop()
l=l[::-1]
while 1<len(l) and l[-2]<1:
    v+=l.pop()*l.pop()
print(v+sum(l))