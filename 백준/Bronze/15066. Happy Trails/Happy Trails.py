from math import*
print(f'{sum(d*sin(a*pi/180)for a,d in[map(int,i.split())for i in open(0)][1:]):.2f}')