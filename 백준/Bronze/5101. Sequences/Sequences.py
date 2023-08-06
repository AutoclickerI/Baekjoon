while(s:=input())!='0 0 0':
    a,b,c=map(int,s.split())
    n=(c-a)//b
    if n*b!=c-a or n<0:print('X')
    else:print(1+n)