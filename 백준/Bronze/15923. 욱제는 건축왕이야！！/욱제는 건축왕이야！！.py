_,*l=open(0)
a=0
for i in range(len(l)):
    p,q,r,s=map(int,(l[i]+l[i-1]).split())
    a+=abs(p+q-r-s)
print(a)