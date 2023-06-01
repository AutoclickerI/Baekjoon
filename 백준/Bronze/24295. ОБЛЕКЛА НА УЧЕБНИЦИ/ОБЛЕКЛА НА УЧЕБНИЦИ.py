p,q,r,s=input().split()
a,b=sorted(map(eval,[p+'.'+q,r+'.'+s]))

p,q,r,s=input().split()
a1,b1=sorted(map(eval,[p+'.'+q,r+'.'+s]))

p,q,r,s=input().split()
a2,b2=sorted(map(eval,[p+'.'+q,r+'.'+s]))

ans=0

if a1-a>=1 and b<=b1:
    ans=1
if a2-a>=1 and b<=b2:
    if ans and a2>a1:
        ans=1
    else:ans=2
print(ans)
if ans==1:print(a1,b1)
if ans==2:print(a2,b2)