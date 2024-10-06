n=int(input())
a=[0]*(n+2)
a[0]=1
a[1]=2*n+2
for i in range(n):a[i+2]=a[i]+2*(n-i)
print(*a)