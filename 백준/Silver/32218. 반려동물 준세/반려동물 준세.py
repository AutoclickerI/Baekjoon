n,*a=map(int,open(0).read().split())
k=1
while any(a):a=[sum(j>a[i]for j in a[i:])for i in range(n)];k+=1
print(k)