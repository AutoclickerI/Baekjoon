n=int(input())
if n%10!=0:
    print(-1)
else:
    a,b,c=0,0,0
    while n>=300:
        a+=1
        n-=300
    while n>=60:
        b+=1
        n-=60
    while n>=10:
        c+=1
        n-=10
    print(a,b,c)