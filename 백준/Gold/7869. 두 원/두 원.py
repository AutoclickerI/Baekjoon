from math import*
x,y,r,z,n,m=map(float,input().split())
d=((x-z)**2+(y-n)**2)**0.5
P=r*r-m*m
if d>r+m:a=0
elif d+min(r,m)<=max(r,m):a=min(r,m)**2*pi
else:p,q=acos((P+d*d)/2/d/r)*2,acos((d*d-P)/2/d/m)*2;a=(r*r*(p-sin(p))+m*m*(q-sin(q)))/2
print('%.3f'%a)