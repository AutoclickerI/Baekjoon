s=int(input())*2
c=0
for x in range(1,s+1):
    if(y:=s//x)<x:break
    z=x**2+y**2
    c+=z**.5%1==0==s%x

print(c)