_,*l=map(int,open(0))
m=a=0
for i in l[::-1]:
    a+=i>m
    m=max(i,m)
print(a)