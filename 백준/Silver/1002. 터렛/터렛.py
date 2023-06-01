for i in range(int(input())):
    a = list(map(int, input().split()))
    d = ((a[3] - a[0])**2 + (a[4] - a[1])**2)**0.5
    r = a[2] + a[5]
    if r < d:
        print(0)
    elif r == d:
        print(1)
    else:
        if d == 0 and a[2] == a[5]:
            print(-1)
        else:
            if abs(a[2] - a[5]) > d:
                print(0)
            elif abs(a[2] - a[5]) == d:
                print(1)
            else:
                print(2)