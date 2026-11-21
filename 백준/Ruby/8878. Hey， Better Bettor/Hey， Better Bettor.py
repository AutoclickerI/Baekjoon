x,p=map(eval,input().split())
a=.0
try:
 for i in range(1,7<<23):W,L=divmod(i,20529);r=100/p-1;n=1-r**-L;n/=r**W+n-1;a=max(a,W*n-L*(1-x/100)*(1-n))
except:0
print(a)