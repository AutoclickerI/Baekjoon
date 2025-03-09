x=input()
n=len(x)
t=int(n**.5)
u=''
while n%t:t-=1
for i in range(t):
 for j in range(n//t):u+=x[i+j*t]
print(u)