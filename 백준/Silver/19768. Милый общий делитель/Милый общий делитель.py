import math
n=math.gcd(*map(int,input().split()))
a=[]
for i in range(1,1+int(n**.5)):
 if n%i<1:a+=i,n//i
print(max(a,key=lambda x:eval('+'.join(str(x)))))