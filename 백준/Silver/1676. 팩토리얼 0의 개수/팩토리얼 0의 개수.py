import math
n=math.factorial(int(input()))
q=0
while n%10==0:
    q+=1;n//=10
print(q)