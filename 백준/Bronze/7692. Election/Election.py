def find_winner(groups, num_candidates):
    candidates = list(range(1, num_candidates + 1))  # 후보자 리스트
    votes = [0] * num_candidates  # 각 후보자의 득표수 리스트

    while len(candidates) > 1:
        # 득표수 초기화
        votes = [0] * num_candidates

        # 1순위 득표수 계산
        for group in groups:
            for pref in group['preferences']:
                if pref in candidates:
                    votes[pref - 1] += group['count']
                    break

        # 최저 득표수 후보 찾기
        min_votes = min(votes[c - 1] for c in candidates)
        
        # 최저 득표수 후보 중 가장 번호가 큰 후보 제거
        for c in reversed(candidates):
            if votes[c - 1] == min_votes:
                candidates.remove(c)
                break

    return candidates[0]

def main():
    while True:
        # 입력 받기
        G, N = map(int, input().split())
        if G == 0 and N == 0:
            break  # 입력 종료 조건

        groups = []
        for _ in range(G):
            data = list(map(int, input().split()))
            Mi = data[0]
            preferences = data[1:]
            groups.append({'count': Mi, 'preferences': preferences})

        # 승자 찾기
        winner = find_winner(groups, N)
        print(winner)

if __name__ == "__main__":
    main()
