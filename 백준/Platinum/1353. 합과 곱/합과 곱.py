from decimal import*
ans=-1
S,P=map(int,input().split())
if S==P:
    ans=1
else:
    prev=0
    cnt=1
    while 1:
        cnt+=1
        val=(S/Decimal(cnt))**cnt
        if val<prev:
            break
        if P<=val:
            ans=cnt
            break
        prev=val
print(ans)