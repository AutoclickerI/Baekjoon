p=1000000007
def z(y,n):
    if n==1:return y
    elif n%2:return x(z(y,n-1),y)
    else:return z(x(y,y),n//2)
def x(a,b):return [[sum([a[i][k]*b[k][j]for k in range(2)])%p for j in range(len(b[0]))]for i in range(2)]
y,u,n=[[1,1],[1,0]],[[1]]*2,int(input());print(1 if n<3 else x(z(y,n-2),u)[0][0])