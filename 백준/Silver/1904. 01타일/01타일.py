a={1:1,2:2};n=int(input())
for i in range(3,n+1):
    a[i]=(a[i-2]+a[i-1])%15746
print(a[n])