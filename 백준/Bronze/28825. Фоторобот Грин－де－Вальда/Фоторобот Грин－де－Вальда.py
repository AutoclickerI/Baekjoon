def check_fotorobot(n, m, photo, constraints):
    # 색상에 따른 허용 가능한 제한 값을 딕셔너리로 정의
    allowed = {
        '.': {0, 1, 2, 3, 4, 5, 6, 7},
        'R': {1, 3, 5, 7},
        'G': {2, 3, 6, 7},
        'B': {4, 5, 6, 7}
    }

    # 각 좌표에 대해 사진과 게시판 제한 비교
    for i in range(n):
        for j in range(m):
            pixel = photo[i][j]       # 사진의 픽셀 값
            constraint = int(constraints[i][j])  # 게시판 제한 값
            # 픽셀이 제한 값에 맞지 않으면 incorrect 출력
            if constraint not in allowed[pixel]:
                return "incorrect"
    
    # 모든 제한을 만족하면 correct 출력
    return "correct"

# 입력 받기
n, m = map(int, input().split())
photo = [input().strip() for _ in range(n)]
constraints = [input().strip() for _ in range(n)]

# 결과 출력
print(check_fotorobot(n, m, photo, constraints))