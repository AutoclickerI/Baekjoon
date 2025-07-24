n,m=map(int,input().split())
print(int((2*min(n,m)+(n!=m))**.5)or'Impossible')