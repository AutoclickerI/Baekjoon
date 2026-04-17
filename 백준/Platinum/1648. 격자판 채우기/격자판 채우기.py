from functools import*
@cache
def f(i,s):return+(n*m<=i)or(f(i+1,s>>1)if s&1else(i<~-n*m and f(i+1,s>>1|1<<m-1))+(~i%m and~s&2and f(i+2,s>>2)))
n,m=map(int,input().split())
print(f(0,0)%9901)