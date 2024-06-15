a=b=c=0
m=10**9+7
for i in map(int,[*open(0)][1].split()):
    if i==1:
        a+=1
    if i==2:
        b=(a+b*2)%m
    if i==3:
        c+=b
print(c%m)