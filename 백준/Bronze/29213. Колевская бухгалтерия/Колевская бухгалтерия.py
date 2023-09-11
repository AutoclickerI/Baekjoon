a,b,c=map(int,input().split())
ans=0
for i in range(c+1):
    for j in range(c+1-i):
        ans+=a+i>b+j
print(ans)