x,b=map(int,input().split())
r=0
i=1
while x:t=[x//b,0-x//-b][x|b<0];r+=(x-b*t)*i;x=t;i*=10
print(r)