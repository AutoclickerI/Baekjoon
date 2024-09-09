def getpos(c):
    for y in 0,1,2:
        for x,t in enumerate(['qwertyuiop','asdfghjkl','zxcvbnm'][y]):
            if c==t:
                return y,x
(ly,lx),_,(ry,rx)=map(getpos,input())
a=0
for i in input():
    y,x=getpos(i)
    if i in'qwertasdfgzxcv':
        a+=abs(y-ly)+abs(x-lx)+1
        ly,lx=y,x
    else:
        a+=abs(y-ry)+abs(x-rx)+1
        ry,rx=y,x
print(a)