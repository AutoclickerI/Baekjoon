n,m=map(int,input().split())
a,b=0,1
for _ in[0]*n:a,b=b%10,a+b
z=[a]
for _ in[0]*(m-n):a,b=b%10,a+b;z+=a,
print(*z,sep='')