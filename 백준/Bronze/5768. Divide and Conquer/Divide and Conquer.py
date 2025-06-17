import sys

def precompute_divisors(max_n: int) -> list[int]:
    """1부터 max_n까지 각 수의 약수 개수를 계산하여 리스트로 반환."""
    div_cnt = [0] * (max_n + 1)
    for d in range(1, max_n + 1):
        for multiple in range(d, max_n + 1, d):
            div_cnt[multiple] += 1
    return div_cnt

def process_queries(div_cnt: list[int]) -> None:
    """표준 입력에서 M, N 쌍을 읽어들여 결과를 출력."""
    for line in sys.stdin:
        M, N = map(int, line.split())
        if M == 0 and N == 0:
            break

        best_x = M
        best_y = div_cnt[M]
        # 구간 [M, N]을 순회하며 최대 약수 개수, 동률 시에는 큰 수 우선
        for x in range(M, N + 1):
            y = div_cnt[x]
            if y > best_y or (y == best_y and x > best_x):
                best_x, best_y = x, y

        print(f"{best_x} {best_y}")

def main():
    MAX_N = 5000
    div_cnt = precompute_divisors(MAX_N)
    process_queries(div_cnt)

if __name__ == "__main__":
    main()
