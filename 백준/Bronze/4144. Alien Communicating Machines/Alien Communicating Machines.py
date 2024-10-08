for _ in range(int(input())):
    *l,z=input().split()
    x,y=map(int,l)
    t=int(z,x)
    a=''
    while 1:
        t,q=divmod(t,y)
        a='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[q]+a
        if t==0:break
    print(a)