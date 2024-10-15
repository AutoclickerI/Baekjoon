while n:=int(input()):
    d = {}
    for _ in[0]*n:
        y, _, m = input().split()
        if d.get(y):
            d[y][0] += 1
            if m == 'Gold':
                d[y][1] += 1
        else:d[y]=[1,m=='Gold']
    a = min(d, key=lambda x: (-d[x][1], x))
    b = min(d, key=lambda x: (-d[x][0], x))
    print(a, b)