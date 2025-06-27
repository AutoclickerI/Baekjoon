import sys

def inverse_mtf(indices):
    # 1. 알파벳 리스트 초기화
    lst = [chr(ord('a') + i) for i in range(26)]
    result = []
    # 2. 각 인덱스 처리
    for idx in indices:
        ch = lst[idx]        # 현재 리스트에서 문자 추출
        result.append(ch)    # 출력에 추가
        # 추출한 문자를 맨 앞으로 이동
        del lst[idx]
        lst.insert(0, ch)
    # 3. 문자열로 결합
    return ''.join(result)

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    T = int(next(it))
    outputs = []
    for _ in range(T):
        n = int(next(it))
        indices = [int(next(it)) for _ in range(n)]
        outputs.append(inverse_mtf(indices))
    sys.stdout.write("\n".join(outputs))

if __name__ == "__main__":
    main()
