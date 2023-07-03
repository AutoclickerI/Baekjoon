l=[0,0,0]
input()
*L,=map(int,input().split())
ans=0
for i in L:
    if i==0:
        ans+=2*l[1]+l[0]+l[2]
    elif i==1:
        ans+=2*l[0]
    else:
        ans+=l[0]
    l[min(i,2)]+=1
print(ans)