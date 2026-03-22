while n:=int(input()):
    l=[]
    for _ in[0]*n:
        s,e=input().replace('.','').split()
        l+=(int(e),s),
    l.sort(key=lambda i:i[0])
    mv=l[-1][0]
    d=[i for v,i in l if v==mv]
    print(*d)