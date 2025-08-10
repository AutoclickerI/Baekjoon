a, b, c, d, k = map(int, input().split())

seen = {}
seq = []
x = a
day = 0

while day < k:
    if x == 0:
        print(0)
        break
    if x in seen:
        # 사이클 발견
        start = seen[x]
        cycle_len = day - start
        remaining = (k - start) % cycle_len
        print(seq[start + remaining])
        break
    seen[x] = day
    seq.append(x)
    day += 1

    # 하루 시뮬레이션
    x = b * x - c
    if x < 0:
        x = 0
    if x > d:
        x = d

else:
    print(x)
