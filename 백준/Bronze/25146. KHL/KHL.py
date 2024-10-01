def calculate_points(n, matches):
    total_points = 0
    is_home_game = True  # 첫 경기는 홈 경기
    
    for match in matches:
        # 각 부분을 '/' 기준으로 분리
        parts = match.split('/')
        
        # 3분기 점수 가져오기
        D1, G1 = map(int, parts[0].split(':'))
        D2, G2 = map(int, parts[1].split(':'))
        D3, G3 = map(int, parts[2].split(':'))
        
        # 정규 시간 총 점수
        D_total = D1 + D2 + D3
        G_total = G1 + G2 + G3
        
        if D_total != G_total:
            # 정규 시간에 승부가 난 경우
            if (D_total > G_total and is_home_game) or (D_total < G_total and not is_home_game):
                total_points += 3  # Medveščak 승리
        else:
            # 연장전이 있거나 승부차기가 있을 경우
            if len(parts) > 3:
                Dp, Gp = map(int, parts[3].split(':'))
                if Dp != Gp:
                    # 연장전에서 승부가 난 경우
                    if (Dp > Gp and is_home_game) or (Dp < Gp and not is_home_game):
                        total_points += 2  # Medveščak 연장전 승리
                    else:
                        total_points += 1  # Medveščak 연장전 패배
                else:
                    # 승부차기로 넘어간 경우
                    Dk, Gk = map(int, parts[4].split(':'))
                    if (Dk > Gk and is_home_game) or (Dk < Gk and not is_home_game):
                        total_points += 1  # Medveščak 승부차기 승리
        
        # 다음 경기는 홈/원정 전환
        is_home_game = not is_home_game
    
    return total_points

# 입력 처리
n = int(input())
matches = [input().strip() for _ in range(n)]

# 결과 출력
print(calculate_points(n, matches))