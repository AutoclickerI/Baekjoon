my=My=mx=Mx=y=x=d=0
dd={(0,0):'.'}
for i in[*open(0)][1]:
    if i=='F':
        dy,dx=[(1,0),(0,-1),(-1,0),(0,1)][d%4]
        y,x=y+dy,x+dx
        my=min(my,y)
        My=max(My,y)
        mx=min(mx,x)
        Mx=max(Mx,x)
        dd[y,x]='.'
    if i=='R':
        d+=1
    if i=='L':
        d-=1
for y in range(my,My+1):
    for x in range(mx,Mx+1):
        print(end=dd.get((y,x),'#'))
    print()