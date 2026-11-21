x,y=map(int,input().split())
d=y-x
f=x>y
d*=-f|1
i=1+f
while i<d:i*=4
print(i*2-2+d)