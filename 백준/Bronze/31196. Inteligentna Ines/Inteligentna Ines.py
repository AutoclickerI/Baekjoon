n=len(x:=input())
t=int(n**.5)
while n%t:t-=1
for i in range(t):
 for j in range(n//t):print(end=x[i+j*t])