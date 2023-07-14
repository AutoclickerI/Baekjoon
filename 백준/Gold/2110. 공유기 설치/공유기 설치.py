n,c,*x=map(int,open(l:=0).read().split())
x.sort()
h=x[-1]
while l<=h:
 m=(l+h)//2;b=1;p=x[0]
 for q in x:
  if q-p>=m:b+=1;p=q
 if b<c:h=m-1
 else:l=m+1
print(h)