from itertools import combinations
n=int(input())
a=[list(map(int,input().split()))for i in range(n)]
l=list(range(n))
p=list(combinations(l,n//2))
z=None
def f(n):
    q=list(combinations(n,2))
    return sum([a[y[0]][y[1]]+a[y[1]][y[0]]for y in q])
for i in range(len(p)//2):
    if z==None:
        z=abs(f(p[i])-f(p[len(p)-1-i]))
    else:
        if z>abs(f(p[i])-f(p[len(p)-1-i])):
            z=abs(f(p[i])-f(p[len(p)-1-i]))
print(z)