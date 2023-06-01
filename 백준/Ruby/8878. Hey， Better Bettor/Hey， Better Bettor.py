x,p=map(float,input().split())
a=0.0
try:
 for W in range(2499):
  for L in range(1,20529):r=(100-p)/p;K=r**-L;n=(1-K)/(r**W-K);a=max(a,W*n-L*(1-x/100)*(1-n))
except:0
print(a)