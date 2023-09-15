d=[(1,0),(0,1),(-1,0),(0,-1)]
for i in open(0):
    c=0
    x,y=310,420
    print('300 420 moveto\n310 420 lineto')
    for i in i[:-1]:
        c-=(i<'V')*2-1
        c%=4
        dx,dy=d[c]
        x+=dx*10
        y+=dy*10
        print(x,y,'lineto')
    print('stroke\nshowpage')