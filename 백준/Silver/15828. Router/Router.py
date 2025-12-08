n,*a,_=map(int,open(0))
b=[]
for x in a:
 if x<1:b.pop(0)
 elif len(b)<n:b+=x,
print(*b)