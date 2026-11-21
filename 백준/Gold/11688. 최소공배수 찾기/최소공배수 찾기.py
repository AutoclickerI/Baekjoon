from math import*
a,b,L=map(int,input().split())
l=lcm(a,b)
if L%l:x=-1
else:
 x=1
 while l<L:l=lcm(l,x);x*=L//l
print(x)