n,m=map(int,input().split())
b=[1]*n
for _ in[0]*~-m:
    t=[1]
    for i in range(1,n):
        t+=t[-1]+b[i]+b[i-1],
    b=t
print(b[-1]%(10**9+7))