ans=0
for _ in[0]*int(input()):
    a,b=map(int,input().split())
    ans=(ans+b*pow(a,-1,10**9+7))%(10**9+7)
print(ans)