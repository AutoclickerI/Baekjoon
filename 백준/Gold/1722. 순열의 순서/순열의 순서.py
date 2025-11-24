import math
N,q,*l=map(int,open(0).read().split())
if q==1:
    x=l[0]-1
    _,*arr=range(N+1)
    ans=[]
    while arr:
        v=math.factorial(len(arr)-1)
        for i in range(len(arr)+1):
            if x<v*i:break
        i-=1
        x-=v*i
        ans+=arr[i],
        del arr[i]
    print(*ans)
else:
    a=0
    while l:
        a+=math.factorial(len(l)-1)*sorted(l).index(l[0])
        del l[0]
    print(a+1)