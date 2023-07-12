n=int(input())
l=sorted(map(int,input().split()))
if n==1:
    print(l[0])
elif n==2:
    print(sum(l)-1)
else:
    t=n//3
    a,l=l[:t],l[t:]
    b,l=l[:t+n%3//2],l[t+n%3//2:]
    print(a[-1]+b[-1]+l[-1]-3)