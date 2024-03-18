R=range
def f(x):
 for j in R(n):
  if x%a[j]<1:return j
 return n
while any(l:=[*map(int,input().split())]):n,l,r=l;a=[int(input())for i in R(n)];print(sum(f(i)&1^1 for i in R(l,r+1)))