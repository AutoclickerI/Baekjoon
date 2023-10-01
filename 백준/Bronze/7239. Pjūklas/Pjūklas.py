input()
l=sorted(map(int,input().split()))
ans=[]
if len(l)%2:ans+=l.pop(0),
while l:
    ans+=l.pop(),l.pop(0)
print(*ans)