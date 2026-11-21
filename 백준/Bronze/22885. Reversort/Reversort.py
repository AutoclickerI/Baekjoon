def reversort_cost(L):
    cost = 0
    # 1-based 인덱싱으로 생각하기 위해 i를 0부터 N-2까지 순회
    for i in range(len(L) - 1):
        # i번째 위치부터 끝까지에서 최소값의 인덱스 찾기
        j = min(range(i, len(L)), key=lambda x: L[x])
        # Reverse(L[i..j])
        L[i:j+1] = reversed(L[i:j+1])
        # 비용 = (j - i + 1)
        cost += (j - i + 1)
    return cost

def main():
    import sys
    input = sys.stdin.readline

    T = int(input())
    for tc in range(1, T+1):
        n = int(input())
        L = list(map(int, input().split()))
        ans = reversort_cost(L)
        print(f"Case #{tc}: {ans}")

if __name__ == "__main__":
    main()