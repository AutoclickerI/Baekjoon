a=input().split('-')
n=sum(list(map(int,a[0].split('+'))))
for i in range(1,len(a)):
    n-=sum(list(map(int,a[i].split('+'))))
print(n)