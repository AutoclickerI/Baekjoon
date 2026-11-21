import sys
sys.setrecursionlimit(9**9)
def f(c,r,k):
 if k>c*r:return 0,
 if k<=r:return 1,k
 i,j=f(r,c-1,k-r)
 return-~j,r-i+1
print(*f(*map(int,open(0).read().split())))