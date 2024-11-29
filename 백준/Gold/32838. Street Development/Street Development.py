L,n=map(int,input().split())
*l,=map(int,input().split())

def check(m):
    # forward
    p=[-float('inf')]*n
    p[0]=l[0]+m
    for i in range(1,n):
        if l[i]-m<=p[i-1]:
            p[i]=l[i]+m-2*max(l[i]-p[i-1],0)
    # backward
    p2=[float('inf')]*n
    p2[-1]=l[-1]-m
    for i in range(n-1)[::-1]:
        if p2[i+1]<=l[i]+m:
            p2[i]=l[i]-m+2*max(p2[i+1]-l[i],0)
    for i in range(n-1):
        if p2[i+1]<=p[i]:
            return True
    return False

s=0
e=L+1
while 1<e-s:
    m=(e+s)//2
    if check(m):
        e=m
    else:
        s=m
print(e)