*l,=map(int,input().split())
*c,=map(int,input().split())
a=0
for _ in[0]*int(input()):
    q,v=map(int,input().split())
    if q==1:
        if all(i>=j*v for i,j in zip(l,c)):
            print(a:=a+v)
            l=[i-v*j for i,j in zip(l,c)]
        else:
            print('Hello, siumii')
    else:
        l[q-2]+=v
        print(l[q-2])