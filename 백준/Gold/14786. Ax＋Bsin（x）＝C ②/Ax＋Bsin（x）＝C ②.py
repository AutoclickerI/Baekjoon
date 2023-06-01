import math
a,b,c=map(int,input().split())
ans=[(c-b)/a,(c+b)/a]
f=lambda x:a*x+b*math.sin(x)
while f(ans[1])-f(ans[0])>10**-9:
    p=sum(ans)/2
    if f(p)>c:
        ans[1]=p
    else:
        ans[0]=p
print(sum(ans)/2)