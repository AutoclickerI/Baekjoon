f=lambda x:sum(map(int,str(x)))
while n:=int(input()):
 i=11
 while f(n)-f(n*i):i+=1
 print(i)