import sys

for line in sys.stdin:
    N, M, K = map(int, line.split())
    if N == M == K == 0:
        break
    deltas = list(map(int, sys.stdin.readline().split()))

    total = current = N
    for r in range(2, M + 1):
        d = deltas[(r - 2) % K]
        current += d
        total += current

    print(total)
