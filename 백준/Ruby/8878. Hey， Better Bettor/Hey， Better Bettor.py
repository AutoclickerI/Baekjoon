x,p=map(float,input().split())
a=0.0
try:
 for W in range(2499):
  for L in range(1,20529):r=100/p-1;n=1-r**-L;n/=(r**W+n-1);a=max(a,W*n-L*(1-x/100)*(1-n))
except:0
print(a)