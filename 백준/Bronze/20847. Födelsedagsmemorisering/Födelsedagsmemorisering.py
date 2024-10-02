def solve():
    N = int(input())  # 친구 수
    friends = {}

    # 친구 정보 입력 받기
    for _ in range(N):
        name, C, birthday = input().split()
        C = int(C)
        # 생일별로 친구를 기록
        if birthday not in friends:
            friends[birthday] = (name, C)
        else:
            # 더 좋아하는 친구(C가 더 큰 친구)를 선택
            if C > friends[birthday][1]:
                friends[birthday] = (name, C)
    
    # 친구들의 이름을 알파벳 순으로 정렬
    selected_friends = sorted(friend[0] for friend in friends.values())
    
    # 출력
    print(len(selected_friends))  # 선택된 친구 수
    for name in selected_friends:
        print(name)

# 문제 해결 함수 호출
solve()