f=lambda:[*map(int,input().split())]
for _ in range(*f()):
    n,=f()
    a=sum(l:=f())
    b=1
    i=0
    while a>b and i<n:b*=l[i];i+=1
    print(['=','SUMA','ILOCZYN'][(a>b)-(a<b)])