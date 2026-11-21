N,M=map(int,input().split())
*l,=map(int,input())
for i in range(N):
    if 9-l[i]<M:
        M-=(10-l[i])%10
        l[i]=0
if M:
    l[-1]+=M%10
print(*l,sep='')