for _ in[0]*int(input()):
    ans=0
    l=[]
    for _ in[0]*int(input()):
        l+=[[*map(int,input().split())]]
    P,Q,R=map(int,input().split())
    for i in l:
        ans+=max(0,i[0]*P-i[1]*Q+i[2]*R)
    print(ans)