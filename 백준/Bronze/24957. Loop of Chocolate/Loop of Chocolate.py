from math import*
(n,r),*l=[[*map(int,i.split())]for i in open(0)]
l+=l[0],
a=n*4*r**3
for i,j in zip(l,l[1:]):d=dist(i,j);a-=(4*r+d)*(r-d/2)**2
print(a*pi/3)