a,b,c,d,e=map(int,open(0).read().split())
D=abs(a-c)+abs(b-d)
print('YN'[D-e&1|(D>e)])