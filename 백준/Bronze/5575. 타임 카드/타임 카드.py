for i in range(3):
    a,b,c,d,e,f=list(map(int,input().split()))
    d-=a;e-=b;f-=c
    if f<0:f+=60;e-=1
    if e<0:e+=60;d-=1
    if d<0:d+=24
    print(d,e,f)