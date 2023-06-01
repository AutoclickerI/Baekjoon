from math import*
x,y,r,z,n,m=map(float,input().split())
d=((x-z)**2+(y-n)**2)**0.5
if d>r+m:a=0
elif d+min(r,m)<=max(r,m):a=min(r,m)**2*pi
else:p=acos((r*r-m*m+d*d)/(2*d*r))*2;q=acos((m*m-r*r+d**2)/(2*d*m))*2;a=(r*r*(p-sin(p))+m*m*(q-sin(q)))/2
print('%.3f'%a)