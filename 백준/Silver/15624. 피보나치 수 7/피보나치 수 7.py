y=[[1]*2,[1,0]]
u=[[1]]*2
n=int(input())
h=range(2)
def z(y,n):
 if n==1:return y
 elif n%2:return x(z(y,n-1),y)
 else:return z(x(y,y),n//2)
def x(a,b):return[[sum([a[i][k]*b[k][j]for k in h])%(10**9+7) for j in range(len(b[0]))]for i in h]
print(1 if n<3 else x(z(y,n-2),u)[0][0])