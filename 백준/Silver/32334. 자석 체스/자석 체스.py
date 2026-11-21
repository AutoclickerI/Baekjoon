def find_best_position(N, D, board):
    # 2차원 누적 합 배열 생성
    prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]
    
    # 2차원 누적 합 계산
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            prefix_sum[r][c] = board[r - 1][c - 1] + prefix_sum[r - 1][c] + prefix_sum[r][c - 1] - prefix_sum[r - 1][c - 1]
    
    # 특정 영역 내 자석 개수 계산 함수
    def count_magnets_in_area(r1, c1, r2, c2):
        # 주어진 좌표가 보드 안에 있는지 확인 (범위를 벗어나면 0으로 취급)
        r1, c1 = max(1, r1), max(1, c1)
        r2, c2 = min(N, r2), min(N, c2)
        return prefix_sum[r2][c2] - prefix_sum[r1 - 1][c2] - prefix_sum[r2][c1 - 1] + prefix_sum[r1 - 1][c1 - 1]

    best_pos = None
    min_magnets = float('inf')

    # 보드 탐색
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if board[r - 1][c - 1] == 0:  # 빈 칸인 경우
                # (r, c)에 자석을 놓았을 때 거리 D 이내에 자석이 있는지 확인
                magnet_count = count_magnets_in_area(r - D, c - D, r + D, c + D)
                if magnet_count == 0:
                    # 붙는 자석이 없는 경우 즉시 승리 가능한 위치
                    print(r, c)
                    return
                else:
                    # 붙는 자석의 개수가 최소인 위치 찾기
                    if magnet_count < min_magnets:
                        min_magnets = magnet_count
                        best_pos = (r, c)

    # 승리할 수 있는 위치가 없으면, 가장 적은 자석을 가져가는 위치 출력
    print(best_pos[0], best_pos[1])
    print(min_magnets)

# 입력 처리
N, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
find_best_position(N, D, board)