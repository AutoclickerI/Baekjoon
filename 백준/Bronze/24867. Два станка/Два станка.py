t=int(input())
p,q=map(int,input().split())
r,s=map(int,input().split())
if p+r<t:
    print(max((t-p)*q+(t-p-r)*s,(t-p-r)*q+(t-r)*s))
elif p<t or r<t:
    print(max((t-p)*q,(t-r)*s))
else:print(0)