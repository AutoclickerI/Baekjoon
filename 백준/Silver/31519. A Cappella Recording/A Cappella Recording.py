n,d,*p=map(int,open(0).read().split())
x=1
s,*p=sorted(p)
for a in p:
 if a-s>d:x+=1;s=a
print(x)