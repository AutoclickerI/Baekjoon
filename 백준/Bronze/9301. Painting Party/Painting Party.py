for T in range(int(input())):
    M=int(input())
    board=eval("['.']*M,"*M)
    for _ in range(int(input())):
        s,*l,c=input().split()
        x,y,w,h=map(int,l)
        if s=='Filled':
            for i in range(x,x+w):
                for j in range(y,y+h):board[i-1][j-1]=c
        else:
            board[x-1][y-1:y+h-1]=[c]*h
            for i in range(x,x+w-2):
                board[i][y-1]=c
                board[i][y+h-2]=c
            board[x+w-2][y-1:y+h-1]=[c]*h
    print(f'Case {T+1}:')
    for i in[*zip(*board)][::-1]:print(*i,sep='')