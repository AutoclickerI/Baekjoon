r=A=1
for z,x in zip(*eval('map(int,input().split()),'*2)):r&=A+z<2;A+=z-x
print('YNeos'[r::2])