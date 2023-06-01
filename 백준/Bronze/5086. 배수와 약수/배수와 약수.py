a,b=map(int,input().split())
while a!=0:
    print('factor'if b%a==0 else'multiple'if a%b==0 else'neither')
    a,b=map(int,input().split())