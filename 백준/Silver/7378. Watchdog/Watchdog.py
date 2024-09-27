f=lambda:(*map(int,input().split()),)
import math
for a in[0]*f()[0]:
    S,H=f()
    h={f()for _ in[0]*H}
    for x in range(1,S):
        for y in range(1,S):
            if{(x,y)}-h:
                d=min(x,S-x,y,S-y)
                if all(d>=math.dist((x,y),i)for i in h):a=x,y;break
        if a:break
    print(*a or['poodle'])