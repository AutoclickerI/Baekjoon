h,w,q,*l=map(int,open(p:=0).read().split())
a=w*h*[0]
m=w*h*[1]
for _ in[0]*q:
 o,x,y=l[p:p+3];b=o<2;p+=3+b
 for i in range(4):
  if m[t:=(x-i//2)*w+y-i%2]:
   m[t]=b
   if b:a[t]=l[p-1]
print(*a)