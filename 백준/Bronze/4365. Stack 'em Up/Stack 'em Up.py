N,*l=map(int,open(0).read().split())
def main():
    suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
    val = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    A = []
    
    # 섞기 매트릭스 입력 받기
    for i in range(N):
        A.append([x - 1 for x in l[52*i:52*-~i]])

    B = list(range(52))  # 초기 덱 (순서대로 0~51)
    C = [0] * 52  # 임시 배열
    tc = 0  # 셔플 횟수 카운트
    
    for i in l[N*52:]:
        k = i - 1  # 현재 사용할 셔플 매트릭스 번호
        for i in range(52):
            C[i] = B[A[k][i]]  # 셔플 진행
        B = C.copy()  # 결과를 B에 저장

        if tc > 0:
            print()  # 카드 출력 사이에 빈 줄 출력

        # 카드 출력
        for x in B:
            print(val[x % 13] + " of " + suit[x // 13])
        
        tc += 1

if __name__ == "__main__":
    main()