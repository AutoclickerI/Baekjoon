N,k=map(int,input().split())
k-=1
n=9
c=1
while n*c<k:
    k-=n*c
    n*=10
    c+=1
v=10**(c-1)
v+=k//c
if N<v:
    print(-1)
else:
    print(str(v)[k%c])