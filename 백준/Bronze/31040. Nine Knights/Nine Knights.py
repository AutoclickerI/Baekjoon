def check(board):
    for i in range(5):
        for j in range(5):
            if board[i][j]=='k':
                for dx,dy in(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2):
                    if 0<=i+dx<5 and 0<=j+dy<5 and board[i+dx][j+dy]=='k':
                        print('invalid')
                        return
    print('valid')
*l,=open(0)
while l:
    _,a,b,c,d,e,*l=l
    check([a,b,c,d,e])