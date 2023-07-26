while(i:=input())>'00':
    p,q,r=map(int,i.split())
    n=p//2+1-q
    if q+r+n>p:print(-1)
    else:print(max(0,n))