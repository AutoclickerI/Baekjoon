n,k=map(int,input().split())
P=10**9+7
def f(n):
 for i in range(a:=1,n+1):a=a*i%P
 return a
def m(x,n):
 return x if n==1 else m(x,n//2)**2%P if n%2==0 else m(x,n//2)**2*x%P
print(f(n)*m(f(k)*f(n-k),P-2)%P)