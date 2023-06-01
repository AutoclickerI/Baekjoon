a=[1,1,2,2,2,8]
b=list(map(int,input().split()))
[print(a[i]-b[i],end=' ')for i in range(6)]