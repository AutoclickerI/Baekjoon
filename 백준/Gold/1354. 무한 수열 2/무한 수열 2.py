m={}
def A(n):
 if(n in m)<1:m[n]=n<1or A(n//P-X)+A(n//Q-Y)
 return m[n]
N,P,Q,X,Y=map(int,input().split())
print(+A(N))