I=input
while n:=int(I()):print(sum(sorted(eval('int(I()),'*n))[1:-1])//(n-2))