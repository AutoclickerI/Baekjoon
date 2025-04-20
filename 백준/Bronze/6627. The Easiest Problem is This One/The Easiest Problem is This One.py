f=lambda n:sum(map(int,str(n)))
while n:=int(input()):
    for i in range(11,1000):
        if f(n)==f(n*i):print(i);break