I=input
for _ in[0]*int(I()):
 c=1e9
 for d,p in sorted([*map(int,I().split())]for _ in[0]*int(I()))[::-1]:c=min(c,d+1)-p
 print(d-c)