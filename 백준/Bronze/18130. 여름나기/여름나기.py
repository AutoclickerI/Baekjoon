def main():
    import sys
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    
    best_cost = None
    best_idx = 0
    
    for i in range(1, N+1):
        P, K, C = map(int, input().split())
        # Q시간 이전까지 지불해야 하는 횟수
        M = (Q - 1) // K
        # 1*C + 2*C + ... + M*C = C * M*(M+1)//2
        extra = C * M * (M + 1) // 2
        total = P + extra
        
        if best_cost is None or total < best_cost:
            best_cost = total
            best_idx = i
    
    print(best_idx, best_cost)

if __name__ == "__main__":
    main()