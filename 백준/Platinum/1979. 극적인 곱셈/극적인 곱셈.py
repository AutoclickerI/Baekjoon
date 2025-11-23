N,K=map(int,input().split())

ans=[K]
addr=0
while ans[-1]*N+addr!=K:
    x=ans[-1]*N+addr
    ans+=x%10,
    addr=x//10
a=''.join(map(str,ans[::-1]))
if'1'<=a:
    print(a)
else:
    print(0)