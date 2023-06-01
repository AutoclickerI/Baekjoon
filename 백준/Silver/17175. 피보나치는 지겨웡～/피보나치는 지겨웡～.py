y=[[1]*2,[1,0]]
u=[[1]]*2
n=int(input())
h=range(2)
z=lambda y,n:y if n==1else x(z(y,n-1),y)if n%2else z(x(y,y),n//2)
x=lambda a,b:[[sum([a[i][k]*b[k][j]for k in h])for j in range(len(b[0]))]for i in h]
print(1if n<2else(2*x(z(y,n-1),u)[0][0]-1)%(10**9+7))