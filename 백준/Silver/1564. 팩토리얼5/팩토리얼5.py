t=0
n=int(input())
a=1
for i in range(1,n+1):
    while~i%2:t+=1;i//=2
    while i%5==0:t-=1;i//=5
    a=a*i%10**5
if t>0:a=a*pow(2,t,10**5)
else:a=a*pow(5,-t,10**5)
print(f'{a%10**5:05d}')