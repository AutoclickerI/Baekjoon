n,m=map(int,input().split())
*l,=range(1,n+1)
ans=[]
c=0
while l:
    c=(c+m-1)%len(l)
    ans+=l.pop(c),
print('<'+str(ans)[1:-1]+'>')