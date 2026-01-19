n,m=map(int,input().split())
l=[]
for _ in[0]*n:
    P,L=map(int,input().split())
    v=sorted(map(int,input().split()))
    if P<L:
        l+=1,
    else:
        l+=v[-L],
l.sort()
c=0
for i in l:
    if i<=m:
        m-=i
        c+=1
print(c)