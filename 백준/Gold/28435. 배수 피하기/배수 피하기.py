N,K=map(int,input().split())
s={}
for i in map(int,input().split()):
    s[i%K]=s.get(i%K,0)+1
ans=1
for i in sorted(s):
    if i*2%K==0:
        ans*=s[i]+1
    elif K-i in s:
        if i*2<K:
            ans*=pow(2,s[i],10**9+7)+pow(2,s[K-i],10**9+7)-1
    else:
        ans*=pow(2,s[i],10**9+7)
print((ans-1-sum(s.values()))%(10**9+7))