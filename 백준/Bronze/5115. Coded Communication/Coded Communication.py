import sys

def main():
    input = sys.stdin.readline
    K = int(input().strip())
    
    for ds in range(1, K+1):
        # 공백 줄이 있을 수 있으므로 처리
        line = input().strip()
        while line == "":
            line = input().strip()
        n, b = map(int, line.split())
        
        valid = [input().strip() for _ in range(n)]
        r = input().strip()
        
        min_flips = b  # 최대 b비트가 다를 수 있음.
        for code in valid:
            # 해밍 거리 계산: 두 문자열의 대응하는 문자가 다르면 1씩 카운트
            diff = sum(1 for i in range(b) if code[i] != r[i])
            if diff < min_flips:
                min_flips = diff
                
        print(f"Data Set {ds}:")
        print(min_flips)
        print()  # 데이터셋 사이 빈 줄

if __name__ == '__main__':
    main()
