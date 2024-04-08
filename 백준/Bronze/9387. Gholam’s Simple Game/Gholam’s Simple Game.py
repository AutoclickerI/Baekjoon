for _ in[0]*int(input()):
    m,n=map(int,input().split())
    *a,=map(int, input().split())
    l=3 in a
    r=a.index(2+l)
    
    t=0
    while n:
        if r==0:l=0
        if r==m-1:l=1
        r+=1-2*l;t+=a[r]<1;n-=1
    print(t)