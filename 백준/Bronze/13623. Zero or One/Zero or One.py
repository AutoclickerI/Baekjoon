a,b,c=input().split()
print('*'if a==b==c else'A'if b==c else'B'if a==c else'C')