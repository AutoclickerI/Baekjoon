n,m=map(int,input().split())
f=lambda k:[n-k,k<2or k&1and-~min(f(k+1),f(k-1))or min(k-n,f(k//2))][n<k]
print(+f(m))