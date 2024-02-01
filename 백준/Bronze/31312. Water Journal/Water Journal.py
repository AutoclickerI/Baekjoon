p,q,r=map(int,input().split())
l=sorted(int(input())for _ in[0]*~-p)
if(l[0],l[-1])==(q,r):
    print(*range(q,r+1))
elif l[0]<q or r<l[-1] or l[0]!=q and l[-1]!=r:
    print(-1)
else:
    print(q*(l[0]>q)+r*(l[-1]<r))