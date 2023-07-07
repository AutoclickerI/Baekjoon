R,C,T=map(int,input().split())
board=[[*map(int,input().split())]for _ in[0]*R]
for _ in[0]*T:
    tmp=[C*[0]for _ in[0]*R]
    for i in range(R):
        for j in range(C):
            dust=max(board[i][j],0)//5
            tmp[i][j]+=board[i][j]
            for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
                if 0<=i+dy<R and 0<=j+dx<C and board[i+dy][j+dx]!=-1:
                    tmp[i+dy][j+dx]+=dust
                    tmp[i][j]-=dust
    c=0
    while c:=c+1:
        if board[c][0]==-1:
            tmp[c][0]=0
            tmp[c]=[-1]+tmp[c]
            k=c
            T=tmp[c].pop()
            while k:=k-1:
                tmp[k][-1],T=T,tmp[k][-1]
            tmp[0]+=[T]
            T=tmp[0].pop(0)
            for i in range(c):
                tmp[i+1][0],T=T,tmp[i+1][0]
            tmp[c][0]=-1
            break
    c+=1
    tmp[c][0]=0
    tmp[c]=[-1]+tmp[c]
    k=R-1
    T=tmp[c].pop()
    for i in range(c+1,R-1):
        tmp[i][-1],T=T,tmp[i][-1]
    tmp[-1]+=[T]
    T=tmp[-1].pop(0)
    while(k:=k-1)!=c:
        tmp[k][0],T=T,tmp[k][0]
    tmp[c][0]=-1
    board=tmp
print(sum(sum(i)for i in board)+2)