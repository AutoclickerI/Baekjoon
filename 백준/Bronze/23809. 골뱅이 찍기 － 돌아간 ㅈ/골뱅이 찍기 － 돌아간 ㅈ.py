n=int(input())
a=['@'*n+'   '*n+'@'*n]*n
b=['@'*n+'  '*n+'@'*n]*n
c=['@@@'*n]*n
print(*a+b+c+b+a)