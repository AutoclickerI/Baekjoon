board=[200*['.']for _ in[0]*200]
x,y=199,0
l=[0]
for _ in[0]*int(input()):
    l+=input(),
for i in input().split():
    w,p,q,r,s=l[int(i)].split()
    for i in range(int(p)):
        for j in range(int(q)):
            board[x-i][y+j]=w
    if'0'<r:
        x+=int(s)-int(p)
        y+=int(q)
    else:
        x-=int(p)
        y+=int(s)-1
board=[j for j in zip(*[i for i in zip(*board)if{*i}-{'.'}])if{*j}-{'.'}]
print(len(board),len(board[0]))
[print(*i,sep='')for i in board]