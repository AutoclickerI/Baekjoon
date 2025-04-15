mod=10**9+7

N=int(input())
l=sorted(map(int,input().split()))

v=0

for i in range(1,N):
    v+=(l[i]-l[0])*pow(2,i-1,mod)
    v%=mod

ans=v

for i in range(1,N):
    diff=l[i]-l[i-1]
    v-=diff
    v*=pow(2,-1,mod)
    v-=diff*(pow(2,N-i-1,mod)-1)
    v%=mod
    ans+=v
    ans%=mod

print(ans)