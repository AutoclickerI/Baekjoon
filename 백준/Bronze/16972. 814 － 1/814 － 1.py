N=16280

def trifill(v):
    l=[]
    f=y=0
    dy=-int((3**.5/2*v)//-1)
    sx=v//2
    while sx*sx+dy*dy<v*v:
        dy+=1
    while y<=N:
        if f:
            x=sx
            while x<N:
                l+=(x,y),
                x+=v
        else:
            x=0
            while x<N:
                l+=(x,y),
                x+=v
        y+=dy
    return l

z=trifill(625)[:813]
for x,y in z:print(x-8140,y-8140)
print(-5640,8119)