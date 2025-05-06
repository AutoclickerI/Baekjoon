def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    eligible = []
    for i in range(1, n+1):
        s, x = input().split()
        x = int(x)
        if s == "TAK":
            eligible.append((i, x))

    # First 10 finalists: the top 10 by original ranking
    group_a = [idx for idx, _ in eligible[:10]]

    # Remove those already selected
    remaining = eligible[10:]
    group_b = []
    for idx, x in remaining:
        if len(group_b) >= 10:
            break
        if x < 2:
            group_b.append(idx)

    finalists = sorted(group_a + group_b)
    print(*finalists)


if __name__ == "__main__":
    main()
