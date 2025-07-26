import sys
import math

def read_input():
    input = sys.stdin.read
    data = input().splitlines()
    return data

def main():
    data = read_input()
    idx = 0

    # number of control points
    n = int(data[idx])
    idx += 1

    # read control point coordinates
    points = []
    for _ in range(n):
        x, y = map(float, data[idx].split())
        points.append((x, y))
        idx += 1

    # number of routes
    m = int(data[idx])
    idx += 1

    for _ in range(m):
        p = int(data[idx])
        idx += 1
        route = list(map(int, data[idx].split()))
        idx += 1

        total_dist = 0.0
        for i in range(p - 1):
            x1, y1 = points[route[i]]
            x2, y2 = points[route[i + 1]]
            dist = math.hypot(x2 - x1, y2 - y1)
            total_dist += dist

        print(round(total_dist))

if __name__ == "__main__":
    main()
