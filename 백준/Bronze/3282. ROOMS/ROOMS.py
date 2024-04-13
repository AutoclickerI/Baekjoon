N,_,*l=map(int,open(0).read().split())
a=[0]*N
f=a.index
for i in l:
 while i:
  try:j=min(i,2);a[f(0)]=j;i-=j
  except:a[f(1)]=2;i-=1
print(*a)