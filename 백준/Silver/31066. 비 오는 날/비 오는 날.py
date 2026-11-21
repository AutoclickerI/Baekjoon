def solve():
    N,M,K=map(int,input().split())
    if M==K==1 and N>1:
        print(-1)
        return
    e=min(K*M,N)
    s=N-e
    step=1
    while s!=0:
        step+=1
        e-=1
        s+=1
        move=min(K*M,N-e)
        step+=1
        s-=move
        e+=move
    print(step)
for _ in[0]*int(input()):
    solve()