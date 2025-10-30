b=[i[::2]for i in open(0)]

def cnt(y,x,dy,dx,c):
    f=v=0
    while 0<=y-dy<19 and 0<=x-dx and b[y-dy][x-dx]==c:
        y-=dy
        x-=dx
        f=1
    while 0<=y<19 and x<19 and b[y][x]==c:
        v+=1
        y+=dy
        x+=dx
    return f,v



for y in range(19):
    for x in range(19):
        for dy,dx in(1,0),(0,1),(1,1),(-1,1):
            for c in'12':
                if b[y][x]==c and cnt(y,x,dy,dx,c)==(0,5):
                    exit(print(c,y+1,x+1))
print(0)