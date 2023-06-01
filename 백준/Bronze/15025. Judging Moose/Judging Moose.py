a,b=map(int,input().split())
if a==b and a+b:print('Even',a+b)
elif a!=b and a+b:print('Odd',max(a,b)*2)
else:print('Not a moose')