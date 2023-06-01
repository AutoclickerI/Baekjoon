a,b=list(map(int,input().split()))
if (a+b)%2==1 or a<b:
    print(-1)
else:
    print(max(abs((a+b)//2),abs((a-b)//2)),min(abs((a+b)//2),abs((a-b)//2)))