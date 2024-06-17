g=lambda x:eval('*'.join(x))
M=int(input())
a,b,c=zip(*eval('input().split(),'*M))
print(c.count('1')%2,g(b)//g(a))