nex={(0,0):(0,1),(0,1):(0,2),(0,2):(1,2),(1,2):(2,2),(2,2):(2,1),(2,1):(2,0),(2,0):(1,0),(1,0):(0,0)}
for _ in[0]*int(input()):
    board=[input()for _ in'000']
    _,*anslist=map(int,input().split())
    x=0
    for i in range(3):
        for j in range(3):
            if board[i][j]=='X':x=(i,j);break
    a=[]
    if not x:
        a+=[8]
    else:
        
        cnt = 0
        for _ in[0]*8:
            i,j=x=nex[x]
            if board[i][j]=='O':
                cnt += 1
            else:
                if cnt:
                    a+=[cnt]
                    cnt = 0
    print(+(sorted(a)==anslist))