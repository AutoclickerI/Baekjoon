ans=0
R,C,M=map(int,input().split())
board=[[(0,0,0)]*C for _ in[0]*R]
for _ in[0]*M:
    r,c,s,d,z=map(int,input().split())
    board[r-1][c-1]=z,s,d
for i in range(C):
    for j in range(R):
        if board[j][i][0]:
            ans+=board[j][i][0]
            board[j][i]=0,0,0
            break
    tmp=[[(0,0,0)]*C for _ in[0]*R]
    for K in range(C):
        for l in range(R):
            k=K
            z,s,d=board[l][k]
            if d<3:
                l+=s*(2*d-3)
                l%=(2*R-2)
                if~-(0<=l<R):
                    l=-l+2*R-2
                    d=3-d
                tmp[l][k]=max(tmp[l][k],(z,s,d))
            else:
                k+=s*(7-2*d)
                k%=(2*C-2)
                if~-(0<=k<C):
                    k=-k+2*C-2
                    d=7-d
                tmp[l][k]=max(tmp[l][k],(z,s,d))
    board=tmp
print(ans)