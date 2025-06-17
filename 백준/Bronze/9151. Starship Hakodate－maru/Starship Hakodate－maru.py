import sys
import bisect

def precompute_sums(limit):
    # 큐브 수와 테트라헤드랄 수 리스트 생성
    cubes = [n**3 for n in range(int(limit**(1/3)) + 1)]
    tetras = [k*(k+1)*(k+2)//6 for k in range(int((6*limit)**(1/3)) + 1)]
    
    # 가능한 모든 합 계산
    sums = set()
    for c in cubes:
        for t in tetras:
            s = c + t
            if s > limit:
                break
            sums.add(s)
    sorted_sums = sorted(sums)
    return sorted_sums

def main():
    LIMIT = 151200
    sorted_sums = precompute_sums(LIMIT)
    
    data = sys.stdin.read().split()
    for line in data:
        m = int(line)
        if m == 0:
            break
        # sorted_sums에서 m 이하의 최댓값을 이분 탐색으로 찾음
        idx = bisect.bisect_right(sorted_sums, m) - 1
        print(sorted_sums[idx])

if __name__ == "__main__":
    main()
