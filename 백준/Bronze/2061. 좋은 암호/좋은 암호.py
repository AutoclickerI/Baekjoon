a,b=map(int,input().split())
h=0
for i in range(2,b):
   if a%i==0:h=i;break
if h:print('BAD',h)
else:print('GOOD')