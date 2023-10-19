D,C,R=map(int,input().split())
C=[int(input())for _ in[0]*C]
ans=R
D+=sum(int(input())for _ in[0]*R)
for i in C:
    if i<=D:
        D-=i
        ans+=1
    else:
        break
print(ans)