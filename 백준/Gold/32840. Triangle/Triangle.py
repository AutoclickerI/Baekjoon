def ccw(ax,ay,bx,by,cx,cy):
    return abs(ax*by+bx*cy+cx*ay-ax*cy-bx*ay-cx*by)

import math

ax,ay,bx,by,cx,cy=map(int,input().split())

gab=math.gcd(abs(ax-bx),abs(ay-by))
gbc=math.gcd(abs(cx-bx),abs(cy-by))
gca=math.gcd(abs(ax-cx),abs(ay-cy))

if 1 in[gab,gbc,gca]:
    print(-1)
else:
    ab=[((ax*~-gab+bx)//gab,(ay*~-gab+by)//gab),((ax+bx*~-gab)//gab,(ay+by*~-gab)//gab)]
    bc=[((bx*~-gbc+cx)//gbc,(by*~-gbc+cy)//gbc),((bx+cx*~-gbc)//gbc,(by+cy*~-gbc)//gbc)]
    ca=[((cx*~-gca+ax)//gca,(cy*~-gca+ay)//gca),((cx+ax*~-gca)//gca,(cy+ay*~-gca)//gca)]
    l=sorted(ccw(*i,*j,*k)for i in ab for j in bc for k in ca)
    print(l[7],l[0])