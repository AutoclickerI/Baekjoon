import math
input()
*l1,=map(int,input().split())
*l2,=map(int,input().split())
g1=l1[0]
for i in l1:g1=math.gcd(g1,i)
g2=l2[0]
for i in l2:g2=math.gcd(g2,i)
l1=[i//g1 for i in l1]
l2=[i//g2 for i in l2]
print(sum(l1),sum(l2)*max(j and 0-i//-j for i,j in zip(l1,l2)))