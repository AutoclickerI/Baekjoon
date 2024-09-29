arr=[(1,0),(0,1),(-1,0),(0,-1)]
y=x=0
d=0
for _ in[0]*int(input()):
    s=input();t=0
    if s=='W':t=4
    if s=='A':t=3
    if s=='S':t=2
    if s=='D':t=1
    if s=='MR':d+=1
    if s=='ML':d-=1
    if t:dy,dx=arr[d+t&3];y+=dy;x+=dx
    dy,dx=arr[d+2&3]
    print(x,y,x+dx,y+dy)