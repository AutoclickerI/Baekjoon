h,m=map(int,input().split())
y=(m-5)%60*12+60
z=(y-60*h+~m)%720+1
print(y//60,y%60,z//60,z%60)