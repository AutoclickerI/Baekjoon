N=int(input())

c = 0

for _ in[0]*N:
    x1, y1, x2, y2 = map(eval,input().split())
    min_x, max_x = sorted([x1, x2])
    c += min_x//1 < max_x//1

print(2 * N / c)