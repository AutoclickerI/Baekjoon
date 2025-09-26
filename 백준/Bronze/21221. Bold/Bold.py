N,M=map(int,input().split())
l=[[*input()]for _ in[0]*N]
for y in range(N)[::-1]:
    for x in range(M)[::-1]:
        if l[y][x]=='#':
            for dy,dx in(1,0),(0,1),(1,1):
                l[y+dy][x+dx]='#'
for i in l:print(*i,sep='')