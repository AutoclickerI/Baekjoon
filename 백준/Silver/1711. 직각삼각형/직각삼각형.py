_,*l=[[*map(int,i.split())]for i in open(0)]
r=0
import math
for y,x in l:
    d={}
    for yy,xx in l:
        yy-=y
        xx-=x
        if yy<0:
            yy*=-1
            xx*=-1
        g=math.gcd(yy,xx)
        if g:
            yy//=g
            xx//=g
            r+=d.get((xx,-yy),0)+d.get((-xx,yy),0)
            d[yy,xx]=d.get((yy,xx),0)+1
print(r)