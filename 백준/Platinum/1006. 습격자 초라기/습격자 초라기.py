def DP(a1,a2,init):
    N=len(a1)
    tb=[3*[float('inf')]for _ in[0]*N]+[[0,0,0]]
    tb[0]=init
    for i in range(1,N):
        tb[i][0]=min(tb[i-1][0]+2,tb[i-1][1]+1+(W<a1[i-1]+a1[i]),tb[i-1][2]+1)
        tb[i][1]=min(tb[i-1][1]+2,tb[i-1][0]+1+(W<a2[i-1]+a2[i]),tb[i-1][2]+1)
        tb[i][2]=min(tb[i-1][2]+1+(W<a1[i]+a2[i]),tb[i-2][2]+2+(W<a1[i-1]+a1[i])+(W<a2[i-1]+a2[i]),tb[i][0]+1,tb[i][1]+1)
    return tb[-2]
    
for T in[0]*int(input()):
    N,W=map(int,input().split())
    *a1,=map(int,input().split())
    *a2,=map(int,input().split())
    m=DP(a1,a2,[1,1,1+(W<a1[0]+a2[0])])[2]
    if a1[0]+a1[-1]<=W:
        m=min(m,DP(a1,a2,[0,1,1])[1]+1)
    if a2[0]+a2[-1]<=W:
        m=min(m,DP(a1,a2,[1,0,1])[0]+1)
    if a1[0]+a1[-1]<=W and a2[0]+a2[-1]<=W:
        a1=a1[1:-1]
        a2=a2[1:-1]
        m=min(m,(DP(a1,a2,[1,1,1+(W<a1[0]+a2[0])])[2]if a1 else 0)+2)
    print(m)