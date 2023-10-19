n=int(input())
t=0
v=1
for i in range(1,n+1):
    while i%2==0:
        i//=2
        t+=1
    while i%5==0:
        i//=5
        t-=1
    v=v*i%10
if t>0:
    print(v*pow(2,t,10)%10)
else:
    print(v*pow(5,-t,10)%10)