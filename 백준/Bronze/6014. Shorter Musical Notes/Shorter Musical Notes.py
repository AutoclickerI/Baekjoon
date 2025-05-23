# Python 3
import sys
from bisect import bisect_right

input = sys.stdin.readline
N, Q = map(int, input().split())
B = [int(input()) for _ in range(N)]

# 누적합
P = [0]
for b in B:
    P.append(P[-1] + b)

out = []
for _ in range(Q):
    T = int(input())
    # P[i] > T 인 최소 i
    idx = bisect_right(P, T)
    out.append(str(idx))

print("\n".join(out))
