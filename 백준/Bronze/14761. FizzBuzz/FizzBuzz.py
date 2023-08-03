x,y,n=map(int,input().split())
for i in range(n):print('Fizz'*(1-~i%x)+'Buzz'*(1-~i%y)or-~i)