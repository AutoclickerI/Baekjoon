import sys
sys.setrecursionlimit(9**6)
A=lambda*x:all(x)
O=lambda*x:any(x)
N=lambda x:not x
n=lambda y,x:x==y[0]
ni=lambda y,x:x in y[0]
a=lambda y,x:x==y[1]
t=lambda y,x:x in y[2:]
L=[input().split()for _ in range(int(input()))]
for _ in[0]*int(input()):f=eval("lambda y:"+("A("+input()+")").replace(")","'))").replace(",","'),").replace(":","(y,'").replace(")')",")"));print(sum(f(y)for y in L))