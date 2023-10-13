input()
l=[(j,i+1)for i,j in enumerate(map(int,input().split()))]
idx=0
ans=[]
while l:
    ans+=l.pop(idx),
    if l:
        idx=(idx+ans[-1][0]-(ans[-1][0]>0))%len(l)
print(*[i for _,i in ans])