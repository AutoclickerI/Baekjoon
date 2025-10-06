H,W=map(int,input().split())
b=[W*[0]for _ in[0]*H]
c=0
for i in input().split():
    for j in range(int(i)):b[~j][c]=1
    c+=1
c=0
def forward(y,x):
    global c
    if b[y][x]==1:
        return 1
    if x+1<W:
        if forward(y,x+1):
            c+=1
            b[y][x]=1
            return 1
    return 0

for y in range(H):
    for x in range(1,W):
        if b[~y][x-1]==1:forward(~y,x)
print(c)