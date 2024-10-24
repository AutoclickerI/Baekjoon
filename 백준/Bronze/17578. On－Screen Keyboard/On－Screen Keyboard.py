d=lambda c:divmod(s.find(c),W)

while'1'<(s:=input()):
    H,W=map(int,s.split())
    s=''.join(eval('input(),'*H))
    y=x=a=0
    for i in input():
        ny,nx=d(i)
        a+=abs(y-ny)+abs(x-nx)+1
        y,x=d(i)
    print(a)