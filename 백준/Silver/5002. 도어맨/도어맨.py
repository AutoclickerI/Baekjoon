n=int(input())
l=[*input()]
cnt=0
ans=0
try:
    while 1:
        if len(l)==1:
            cnt+='MW'.index(l[0])*2-1
            l.pop(0)
        elif abs(cnt+'MW'.index(l[0])*2-1)<abs(cnt+'MW'.index(l[1])*2-1):
            cnt+='MW'.index(l[0])*2-1
            l.pop(0)
        else:
           cnt+='MW'.index(l[1])*2-1
           l.pop(1)
        assert -n<=cnt<=n
        ans+=1
except:
    print(ans)