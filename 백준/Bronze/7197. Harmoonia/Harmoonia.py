def find_parallel_fifths(N, K, notes):
    # 결과를 저장할 리스트
    result = []

    # 각 두 연속된 음 사이에서 병행 5도를 검사
    for i in range(N - 1):
        for s in range(K):
            for t in range(s + 1, K):
                # 두 음의 차이를 계산하고, 12로 나눈 나머지가 7인지 확인
                diff1 = notes[i][s] - notes[i][t]
                diff2 = notes[i + 1][s] - notes[i + 1][t]
                
                if diff1 % 12 == 7 and diff2 % 12 == 7 and notes[i][s]!=notes[i+1][s] and notes[i][t]!=notes[i + 1][t]:
                    result.append((i + 1, s + 1, t + 1))

    # 병행 5도가 없는 경우 "POLE" 출력
    if not result:
        print("POLE")
    else:
        # 병행 5도가 있는 경우 결과 출력
        for res in result:
            print(res[0], res[1], res[2])

# 입력 받기
N, K = map(int, input().split())
notes = [list(map(int, input().split())) for _ in range(N)]

# 병행 5도 찾기
find_parallel_fifths(N, K, notes)