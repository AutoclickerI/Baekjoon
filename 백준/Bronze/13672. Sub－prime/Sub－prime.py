f=lambda:[*map(int,input().split())]
while l:=f()[1]:
 a=f()
 for i in range(l):x,y,z=f();a[x-1]-=z;a[y-1]+=z
 print('SN'[min(a)<0])