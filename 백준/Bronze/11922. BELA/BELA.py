import sys

def bela_score():
    input = sys.stdin.readline
    # 1) N과 우위 슈트 B 읽기
    N, B = input().split()
    N = int(N)
    
    # 2) 카드별 점수 테이블 정의
    score_dom = {'A':11, 'K':4, 'Q':3, 'J':20, 'T':10, '9':14, '8':0, '7':0}
    score_non = {'A':11,'K':4,'Q':3,'J':2,'T':10,'9':0,'8':0,'7':0}
    
    total = 0
    # 3) 4N장 카드 읽어서 합산
    for _ in range(4 * N):
        card = input().strip()
        rank, suit = card[0], card[1]
        if suit == B:
            total += score_dom[rank]
        else:
            total += score_non[rank]
    
    # 4) 결과 출력
    print(total)

if __name__ == '__main__':
    bela_score()
