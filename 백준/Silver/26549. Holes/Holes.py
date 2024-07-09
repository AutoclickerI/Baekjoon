def DFS(y,x):
    b[y][x]='#'
    s=0
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        if b[y+dy][x+dx]=='.':
            s+=1+DFS(y+dy,x+dx)
    return s
for _ in[0]*int(input()):
    r,c=map(int,input().split())
    b=eval('[*input()],'*r)
    se=0
    sp=0
    for i in range(1,r-1):
        for j in range(1,c-1):
            if b[i][j]=='.':
                se+=1
                sp+=DFS(i,j)+1
    print(se,'section'+'s'*(se!=1)+',',sp,'space'+'s'*(sp!=1))