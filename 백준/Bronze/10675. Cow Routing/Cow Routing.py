f=lambda:map(int,input().split())
*A,n=f()
y=999
for x in[0]*n:
 c,r=f()
 for i in f():
  x+=i==A[x]
  if x>1:y=min(y,c);break
print(-(998<y)or y)