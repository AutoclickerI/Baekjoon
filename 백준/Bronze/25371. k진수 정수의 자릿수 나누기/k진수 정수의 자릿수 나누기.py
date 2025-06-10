n,k=map(int,input().split())
def f(n,k,t=''):
 while n:t=str(n%k)+t;n//=k
 return t
print(f(eval(f(n,k).replace(*'0+')+'+0'),k))