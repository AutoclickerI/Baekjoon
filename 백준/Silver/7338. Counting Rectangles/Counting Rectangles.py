from itertools import*
for _ in range(int(input())):
    h=[]
    v=[]
    for _ in range(int(input())):
        x1, y1, x2, y2 = map(int, input().split())
        if x1 == x2:
            v+=(x1,*sorted((y1, y2))),
        else:
            h+=(y1,*sorted((x1,x2))),
    h_to_v = {(y,x1,x2):{(x,y1,y2) for x,y1,y2 in v if x1<=x<=x2 and y1<=y<=y2} for y,x1,x2 in h}
    ans = 0
    for a, b in combinations(h_to_v.values(), 2):
        k = len(a & b)
        ans += k * (k - 1)
    print(ans >> 1)