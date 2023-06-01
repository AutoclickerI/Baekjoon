import math
p=10**9+7
y=[[1,1],[1,0]]
u=[[1]]*2
h=range(2)
def z(y,n):
 if n==1:return y
 elif n%2:return x(z(y,n-1),y)
 else:return z(x(y,y),n//2)
def x(a,b):return [[sum([a[i][k]*b[k][j]for k in h])%p for j in range(len(b[0]))]for i in h]
def f(n):return 1 if n<3 else x(z(y,n-2),u)[0][0]
for i in range(int(input())):
    k,l=list(map(int,input().split()))
    print(f(math.gcd(k,l)))