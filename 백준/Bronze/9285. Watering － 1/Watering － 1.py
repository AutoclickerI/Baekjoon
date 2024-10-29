H,W,*board=open(0).read().split()

v=[[*i]for i in board]

W,H=map(int,[W,H])

def is_wall(y,x):
    return is_valid_pos(y,x) and (y%6==5 or x%6==5)
def is_valid_pos(y,x):
    return 0<=y<len(board)and 0<=x<len(board[0])
def is_valid(y,x):
    return is_valid_pos(y,x) and not is_wall(y,x)
def get_cell_start_pos(y,x):
    return y//6*6,x//6*6
def count_empty(y,x):
    try:
        a=0
        for dy in range(5):
            for dx in range(5):
                a+=v[y+dy][x+dx]=='.'
        return a
    except:
        print(y,x)

def color(y,x,s,idx,inv=False):
    if not (inv or all(is_valid(y+dy,x+dx) and v[y+dy][x+dx]=='.'for dy,dx in s)):
        return False
    for dy,dx in s:
        if inv:
            v[y+dy][x+dx]='.'
        else:
            v[y+dy][x+dx]='abcdefgh'[idx]
    return True

def work(y,x,order,idx):
    if order==25:
        if count_empty(y,x)<1:
            raise
        else:
            return
    if v[y+order//5][x+order%5]!='.':
        work(y,x,order+1,idx)
    else:
        for s in[(0,0),(1,0),(1,-1)],[(0,0),(1,0),(2,0)],[(0,0),(1,0),(1,1)],[(0,0),(0,1),(1,0)],[(0,0),(0,1),(1,1)],[(0,0),(0,1),(0,2)]:
            if color(y+order//5,x+order%5,s,idx):
                work(y,x,order+1,idx+1)
                color(y+order//5,x+order%5,s,idx,True)

def fill(y,x):
    try:
        work(y,x,0,0)
    except:
        return
    raise

for y in range(H):
    for x in range(W):
        start_pos_y=y*6
        start_pos_x=x*6
        empty=count_empty(start_pos_y,start_pos_x)
        if empty%3==1:
            if is_valid(start_pos_y,start_pos_x+7):
                for dy in[0,2,4]:
                    if all(i=='.'for i in[v[start_pos_y+dy][start_pos_x+4],v[start_pos_y+dy][start_pos_x+6],v[start_pos_y+dy][start_pos_x+7]]):
                        v[start_pos_y+dy][start_pos_x+4]=v[start_pos_y+dy][start_pos_x+6]=v[start_pos_y+dy][start_pos_x+7]='xz'['z'!=v[start_pos_y+dy-1][start_pos_x+6]]
                        v[start_pos_y+dy][start_pos_x+5]='_'
                        break
            elif is_valid(start_pos_y+7,start_pos_x):
                for dx in[0,2,4]:
                    if all(i=='.'for i in[v[start_pos_y+4][start_pos_x+dx],v[start_pos_y+6][start_pos_x+dx],v[start_pos_y+7][start_pos_x+dx]]):
                        v[start_pos_y+4][start_pos_x+dx]=v[start_pos_y+6][start_pos_x+dx]=v[start_pos_y+7][start_pos_x+dx]='z'
                        v[start_pos_y+5][start_pos_x+dx]='_'
                        break
            else:
                raise
        if empty%3==2:
            if is_valid(start_pos_y,start_pos_x+7):
                for dy in[0,2,4]:
                    if all(i=='.'for i in[v[start_pos_y+dy][start_pos_x+4],v[start_pos_y+dy][start_pos_x+6],v[start_pos_y+dy][start_pos_x+3]]):
                        v[start_pos_y+dy][start_pos_x+4]=v[start_pos_y+dy][start_pos_x+6]=v[start_pos_y+dy][start_pos_x+3]='xz'['z'!=v[start_pos_y+dy-1][start_pos_x+6]]
                        v[start_pos_y+dy][start_pos_x+5]='_'
                        break
            elif is_valid(start_pos_y+7,start_pos_x):
                for dx in[0,2,4]:
                    if all(i=='.'for i in[v[start_pos_y+4][start_pos_x+dx],v[start_pos_y+6][start_pos_x+dx],v[start_pos_y+3][start_pos_x+dx]]):
                        v[start_pos_y+4][start_pos_x+dx]=v[start_pos_y+6][start_pos_x+dx]=v[start_pos_y+3][start_pos_x+dx]='z'
                        v[start_pos_y+5][start_pos_x+dx]='_'
                        break
            else:
                raise
        fill(start_pos_y,start_pos_x)
for i in v:
    print(''.join(i))