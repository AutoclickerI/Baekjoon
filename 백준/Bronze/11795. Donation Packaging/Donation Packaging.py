a=b=c=0
for _ in[0]*int(input()):
    p,q,r=map(int,input().split())
    a+=p;b+=q;c+=r
    if min(a,b,c)>29:
        print(m:=min(a,b,c))
        a-=m
        b-=m
        c-=m
    else:
        print('NO')