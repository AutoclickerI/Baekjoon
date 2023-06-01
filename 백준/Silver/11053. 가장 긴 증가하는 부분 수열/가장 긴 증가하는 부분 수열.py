n=int(input())
a=list(map(int,input().split()))
h=[1]*n
for i in range(1,n):
    try:h[i]=max([h[j] for j in range(i)if a[j]<a[i]])+1
    except:0
print(max(h))