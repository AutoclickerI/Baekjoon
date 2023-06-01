h=range(9);a=[list(input())for i in h];b=[(i,j)for i in h for j in h if a[i][j]=='0']
def c(i,j):
 x=a[i][j]
 for k in h:
  if(x==a[i][k]and j!=k)or(x==a[k][j]and i!=k)or(x==a[i//3*3+k//3][j//3*3+k%3]and(i//3*3+k//3!=i or j//3*3+k%3!=j)):return 1
def f(n):
 p,q=b[n]
 for i in h:
  a[p][q]=str(i+1)
  if c(p,q)!=1:f(n+1)
 a[p][q]='0'
try:f(0)
except:[print(''.join(p))for p in a]