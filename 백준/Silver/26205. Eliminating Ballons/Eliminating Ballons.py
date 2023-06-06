input()
d={}
ans=0
for i in map(int,input().split()):
    if i in d and d[i]:
        d[i]-=1
    else:
        ans+=1
    d[i-1]=d.get(i-1,0)+1
print(ans)