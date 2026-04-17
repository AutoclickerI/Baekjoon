from functools import*
m,n=sorted(map(int,input().split()))
@cache
def f(p,b):return b<1if p==m*n else f(p+1,b>>1)if b&1else f(p+1,b>>1|1<<m-1)+(-~p%m>0==b&2and f(p+2,b>>2))
print(f(0,0)%9901)