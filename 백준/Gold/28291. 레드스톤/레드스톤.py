ck=1
t=0
p=2
i,_,*j=open(0)
W,H=map(int,i.split())
board=[H*[(0,0)]for _ in[0]*W]
lamp=set()
for i in j:
    P,q,r=eval(i[12:].replace(*' ,'))
    if P==2:lamp.add((q,r))
    else:board[q][r]=(16*P,1)
for _ in[0]*15:
 for i in range(W):
  for j in range(H):
   for dx,dy in(-1,0),(0,1),(0,-1),(1,0):
    if W>i+dy>=0<=j+dx<H:p,q=board[i+dy][j+dx];board[i][j]=max(board[i][j],(p*q-1,board[i][j][1]))
for i,j in lamp:(0,0)==board[i][j]and exit(print('failed'))
print('success')