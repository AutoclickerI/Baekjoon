p,q,r,s,n=map(int,input().split())
y=[[p,q],[1,0]]
u=[[s],[r]]
h=range(2)
z=lambda y,n:y if n==1 else x(z(y,n-1),y)if n%2 else z(x(y,y),n//2)
x=lambda a,b:[[sum([a[i][k]*b[k][j]for k in h])%100 for j in range(len(b[0]))]for i in h]
print(f'{u[n][0]if n<2 else x(z(y,n-1),u)[0][0]:02d}')