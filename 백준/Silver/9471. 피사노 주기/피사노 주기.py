for i in[*open(0)][1:]:
    t,n=map(int,i.split())
    a=b=1
    c=1
    while a!=1 or b!=0:
        a,b=(a+b)%n,a
        c+=1
    print(t,c)