N,L=map(int,input().split())
c=-1,
for d in range(100,L-1,-1):a=N-d*~-d//2;c=range(a//d,a//d+(1>a%d<=a)*d)or c
print(*c)