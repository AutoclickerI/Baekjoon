from functools import*
n,m=map(int,input().split())
f=cache(lambda k,s:(~-k%m>s&3<1and f(k-2,s>>2))+f(k-1,s>>1|~s%2<<m-1)if k else s<1)
print(f(n*m,0)%9901)