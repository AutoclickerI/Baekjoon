n=int(input())
a=sorted([list(map(int,input().split()))for i in range(n)])
h=[1]*n
for i in range(1,n):
    try:h[i]=max([h[j] for j in range(i)if a[j][1]<a[i][1]])+1
    except:0
print(n-max(h))