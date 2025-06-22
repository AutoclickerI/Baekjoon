import sys

def min_final_score(p, t, m):
    # 가중치 * 점수의 합을 100배 스케일로 환산
    # 목표: 15p + 20t + 25m + 40F >= 9000
    need = 9000 - (15*p + 20*t + 25*m)
    if need <= 0:
        return 0      # 이미 평균 90 이상
    # F >= need / 40 을 올림
    F = (need + 40 - 1) // 40
    if F > 100:
        return None   # 불가능
    return F

def main():
    data = sys.stdin.read().split()
    tc = int(data[0])
    idx = 1
    for _ in range(tc):
        p, t, m = map(int, data[idx:idx+3])
        idx += 3
        ans = min_final_score(p, t, m)
        print(ans if ans is not None else "impossible")

if __name__ == "__main__":
    main()
