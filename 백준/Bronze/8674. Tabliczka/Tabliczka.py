a=list(map(int,input().split()))
a.sort()
print(0 if a[0]*a[1]%2==0 else a[0])