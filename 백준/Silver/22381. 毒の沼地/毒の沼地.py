import sys
f=lambda:map(int,sys.stdin.readline().split())
dist=lambda a,b:max(0,a-C,A-a)+max(0,b-D,B-b)
while N:=int(input()):
    A,B,C,D=f()
    x,y=f()
    ans = 0
    for _ in range(N):
        nx,ny=f()
        if A <= x <= C and B <= y <= D:
            ans += dist(nx, ny)
        elif A <= nx <= C and B <= ny <= D:
            ans += dist(x, y) - 1
        else:
            dx, dy = (nx > x) - (nx < x), (ny > y) - (ny < y)
            cnt1 = dist(nx, ny) + dist(x, y) - 1
            cnt2 = 0
            while x != nx:
                x += dx
                cnt2 += not (A <= x <= C and B <= y <= D)
            while y != ny:
                y += dy
                cnt2 += not (A <= x <= C and B <= y <= D)
            ans += min(cnt1, cnt2)
        x, y = nx, ny
    print(ans)