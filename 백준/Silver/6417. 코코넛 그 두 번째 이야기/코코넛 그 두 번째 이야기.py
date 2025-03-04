def max_people(N):
    # 최대 사람의 수는 보통 10부터 2까지 검사 (문제 조건상 N이 1,000,000 이하이므로 이 범위면 충분)
    for k in range(10, 1, -1):
        M = N
        valid = True
        for _ in range(k):
            # 각 단계에서, (M - 1)이 k로 나누어 떨어져야 함
            if (M - 1) % k != 0:
                valid = False
                break
            # 한 사람의 몫을 제거하고 남은 코코넛 수 갱신
            M = M - 1 - (M - 1) // k
        # 마지막 남은 코코넛이 k로 나누어 떨어져야 함
        if valid and M % k == 0:
            return k
    return 0

# 입력을 여러 케이스에 대해 처리 (N = -1이면 종료)
while True:
    try:
        line = input().strip()
        if not line: 
            continue
        N = int(line)
        if N == -1:
            break
        k = max_people(N)
        if k:
            print(f"{N} coconuts, {k} people and 1 monkey")
        else:
            print(f"{N} coconuts, no solution")
    except EOFError:
        break
