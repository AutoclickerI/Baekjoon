x,y=map(int,input().split())
d=y-x
f=x>y
d*=1-2*f
i=1+f
while i<d:i*=4
print(i*2-2+d)