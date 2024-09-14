h,m=map(int,input().split())
x=60*h+m
y=(m*12-60)%720+60
print(y//60,y%60,*divmod((y+~x)%720+1,60))