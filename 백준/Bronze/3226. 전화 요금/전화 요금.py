import re
p=0
for i in range(int(input())):
 x,y,d=map(int,re.findall('\d+',input()));t=60*x+y
 for i in range(t,t+d):p-=5*~(419<i<1140)
print(p)