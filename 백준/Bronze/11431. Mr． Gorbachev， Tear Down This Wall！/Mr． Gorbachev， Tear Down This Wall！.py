g=lambda:[*map(int,input().split())]
for T in range(int(input())):
    n, s, p = g()  
    ans = 0
    points = [g() for _ in range(n+1)]
    for i in range(n):
        x, y = points[i]
        a, b = points[i+1]
        ans += abs(x - a) + abs(y-b)
    print(f'Data Set {T+1}:\n{0-ans*s//-p}\n')