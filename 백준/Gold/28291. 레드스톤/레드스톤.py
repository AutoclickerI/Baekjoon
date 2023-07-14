redstone_block=0
redstone_dust=1
redstone_lamp=2
W,H=map(int,input().split())
board=[H*[(0,0)]for _ in[0]*W]
lamp=set()
for _ in[0]*int(input()):
    p,q,r=eval(input().replace(*' ,'))
    if p==2:
        lamp.add((q,r))
    elif p==1:
        board[q][r]=(0,1)
    else:
        board[q][r]=(16,1)
for _ in[0]*15:
    for i in range(W):
        for j in range(H):
            for dx,dy in(-1,0),(0,1),(0,-1),(1,0):
                if 0<=i+dy<W and 0<=j+dx<H:
                    p,q=board[i+dy][j+dx]
                    board[i][j]=max(board[i][j],(p*q-1,board[i][j][1]))
for i,j in lamp:
    if board[i][j][0]==0:
        exit(print('failed'))
print('success')