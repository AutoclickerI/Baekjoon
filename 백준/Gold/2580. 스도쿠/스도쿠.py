def f(k):
 k==len(z)<exit(print(*a));r,c=z[k];s={*R(1,10)};x,y=r//3*3,c//3*3
 for i in R(9):s-={a[r*9+i],a[i*9+c]}
 s-={a[i*9+j+y]for i in R(x,x+3)for j in R(3)}
 for n in s:a[t:=r*9+c]=n;f(k+1);a[t]=0
R=range
*a,=map(int,open(0).read().split())
z=[(k//9,k%9)for k in R(81)if a[k]<1]
f(0)