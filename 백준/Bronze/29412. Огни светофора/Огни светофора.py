g,gb,y,r,ry,t=map(int,open(0).read().split())
s = g + gb + y + r + ry
R=Y=G=0
while t:
    t-=1
    rem = t % s
    if rem < g:
        G += 2
    elif rem < g + gb:
        G += 1
    elif rem < g + gb + y:
        Y += 1
    elif rem < g + gb + y + r:
        R += 1
    else:
        R += 1
        Y += 1
print(R,Y,G//2)

