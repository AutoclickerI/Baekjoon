n=int(input())-1
b,a=[list(map(int,input().split()))for i in range(2)]
for i in range(1,n):
    if a[i]>a[i-1]:a[i]=a[i-1]
print(sum([a[i]*b[i]for i in range(n)]))