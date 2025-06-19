import sys

def star_arrangements(S):
    patterns = []
    # 1) x = y
    for x in range(2, S//2 + 1):
        if S % x == 0:
            if S // x >= 2:
                patterns.append((x, x))
    # 2) x = y + 1
    for y in range(1, S//2 + 1):
        x = y + 1
        total = x + y
        # 짝수 행
        if S % total == 0:
            k = S // total
            if k >= 1:
                patterns.append((x, y))
                continue
        # 홀수 행
        if (S - x) % total == 0:
            k = (S - x) // total
            if k >= 1:
                patterns.append((x, y))
    # 정렬 및 중복 제거
    patterns = sorted(set(patterns))
    return patterns

def main():
    S = int(sys.stdin.readline().strip())
    pats = star_arrangements(S)
    print(f"{S}:")
    for x, y in pats:
        print(f"{x},{y}")

if __name__ == "__main__":
    main()
