def find_combinations(pt, p1, p2):
    # 센트 단위로 변환 (소수점 오차 방지용)
    pt = int(round(pt * 100))
    p1 = int(round(p1 * 100))
    p2 = int(round(p2 * 100))

    results = []

    # x는 피타 개수, 0부터 pt까지 시도
    for x in range(pt // p1 + 1):
        remaining = pt - p1 * x
        if remaining % p2 == 0:
            y = remaining // p2
            results.append((x, y))

    if results:
        for x, y in results:
            print(f"{x} {y}")
    else:
        print("none")

# 입력 처리
line = input()
pt_str, p1_str, p2_str = line.strip().split()
find_combinations(float(pt_str), float(p1_str), float(p2_str))
