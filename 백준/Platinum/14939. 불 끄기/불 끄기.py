b=[[*input()]for _ in[0]*10]

def complement(s):
    return'#O'[s!='O']

def apply(y,x):
    for dy,dx in(-1,0),(0,1),(1,0),(0,-1),(0,0):
        ny,nx=y+dy,x+dx
        if 0<=ny<10 and 0<=nx<10:
            b[ny][nx]=complement(b[ny][nx])        

def DFS(step):
    if step==90:
        if {*b[-1]}=={'#'}:
            return 0
        return -1
    y,x=step//10+1,step%10
    f=b[y-1][x]=='O'
    if f:
        apply(y,x)
    ret=DFS(step+1)
    if f:
        apply(y,x)
    if ret<0:
        return -1
    return f+ret

mv=101

for i in range(2**10):
    for x,v in enumerate(f'{i:010b}'):
        v=='1'!=apply(0,x)
    v=DFS(0)
    if 0<=v:
        mv=min(v+i.bit_count(),mv)
    for x,v in enumerate(f'{i:010b}'):
        v=='1'!=apply(0,x)

print(mv if mv!=101 else -1)