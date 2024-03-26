N,M,L,T,K=map(int,input().split())
if T<20*(max(N,M)-1)+K-15:
    print('SAD')
    exit()
board=[input()for _ in[0]*N]
prevt=[M*[0]for _ in[0]*N]
nextt=[M*[0]for _ in[0]*N]
visited=[M*[0]for _ in[0]*N]
cur_t=0
t=[[[*map(int,input().split())]for _ in[0]*int(input())]for _ in[0]*L]
prevr=-1
 
from collections import deque
dq_to_store=deque([(1,1,-5)])
dq_to_school=deque()
flag=0
def setteacher(board_t, cur_time):
    for i in t:
        x,y=i[cur_time%len(i)]
        for dx in-1,0,1:
            for dy in-1,0,1:
                if 0<x+dx<=N and 0<y+dy<=M:
                    board_t[x+dx-1][y+dy-1]=1
setteacher(nextt,0)
def printer():
    print('--prev')
    for i in prevt:
        print(*i)
    print('--next')
    for i in nextt:
        print(*i)
while dq_to_store:
    x,y,r=dq_to_store.popleft()
    #if(x,y)==(28,29):raise
    if r!=prevr:
        prevr=r
        prevt=nextt
        nextt=[M*[0]for _ in[0]*N]
        visited=[M*[0]for _ in[0]*N]
        setteacher(nextt,r//10+2)
    if T<r:
        break
    if (x,y)==(N,M):
        nextt=[M*[0]for _ in[0]*N]
        setteacher(nextt,((r+K-6)//10*10+5)//10+1)#test add
        prevr=-1
        dq_to_school.append((N,M,(r+K-6)//10*10+5))
        break
    for dx in-1,0,1:
        for dy in-1,0,1:
            if ((x+dx,y+dy)==(1,1) or(x+dx,y+dy)==(N,M)or 0<x+dx<=N and 0<y+dy<=M and prevt[x+dx-1][y+dy-1]==nextt[x+dx-1][y+dy-1]==0 and board[x+dx-1][y+dy-1]=='.')and visited[x+dx-1][y+dy-1]==0:
                visited[x+dx-1][y+dy-1]=1
                dq_to_store.append((x+dx,y+dy,r+10))
while dq_to_school:
    x,y,r=dq_to_school.popleft()
    if r!=prevr:    
        prevr=r
        prevt=nextt
        nextt=[M*[0]for _ in[0]*N]
        visited=[M*[0]for _ in[0]*N]
        setteacher(nextt,r//10+2)
    if T<r:
        break
    if x==y==1:
        flag=1
        break
    for dx in-1,0,1:
        for dy in-1,0,1:
            if ((x+dx,y+dy)==(1,1) or(x+dx,y+dy)==(N,M)or 0<x+dx<=N and 0<y+dy<=M and prevt[x+dx-1][y+dy-1]==nextt[x+dx-1][y+dy-1]==0 and board[x+dx-1][y+dy-1]=='.')and visited[x+dx-1][y+dy-1]==0:
                visited[x+dx-1][y+dy-1]=1
                dq_to_school.append((x+dx,y+dy,r+10))
if flag:
    print('YUMMY')
else:
    print('SAD')