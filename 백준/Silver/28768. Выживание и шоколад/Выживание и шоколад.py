n,m=map(int,input().split())
def s(a,b):
 while~a%2>0<b>a//2:a//=2;b*=2
 return a+b
print(2*max(s(n,m),s(m,n)))