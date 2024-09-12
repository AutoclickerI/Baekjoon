from heapq import heappush,heappop
def solve():
    board=eval('input(),'*8)
    c=eval('[float("inf")]*8,'*8)
    hq=[]
    for y in range(8):
        for x in range(8):
            if board[y][x]=='S':
                heappush(hq,(0,y,x))
                c[y][x]=0
    while 1:
        v,y,x=heappop(hq)
        if c[y][x]<v:
            continue
        if board[y][x]=='E':
            break
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            if 0<=y+dy<8>x+dx>=0 and v+(board[y+dy][x+dx]=='M')<c[y+dy][x+dx]:
                c[y+dy][x+dx]=v+(board[y+dy][x+dx]=='M')
                heappush(hq,(c[y+dy][x+dx],y+dy,x+dx))
    print(c[y][x])
try:
    while True:
        solve()
        try:
            input()
        except:
            break
except:
    print(5)