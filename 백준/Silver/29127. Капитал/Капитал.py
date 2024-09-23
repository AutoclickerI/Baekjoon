a,n=map(int,input().split())
if 9*n<a:
    print(-1)
else:
    z=[]
    for _ in range(n):t=min(a,9);a-=t;z+=t,
    print(*z,sep='')