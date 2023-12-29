from datetime import*
input()
l={*input(),'-'}
p,q,r=map(int,input().split('.'))
d=date(r,q,p)
p,q,r=map(int,input().split('.'))
d2=date(r,q,p)
ans=0
while 1:
    ans+={*str(d)}&l=={*str(d)}
    if d2 == d:
        break
    d+=timedelta(days=1)
print(ans)