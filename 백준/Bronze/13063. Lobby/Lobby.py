while(i:=input())>'00':
    p,q,r=map(int,i.split());n=p//2+1-q
    print(-(q+r+n>p)or max(0,n))