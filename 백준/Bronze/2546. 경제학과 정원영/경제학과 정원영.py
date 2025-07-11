import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1

    out = []
    for _ in range(t):
        # 빈 줄이 있을 수 있으므로 건너뛰기
        while data[idx] == '':
            idx += 1
        N = int(data[idx]); M = int(data[idx+1])
        idx += 2

        C = list(map(int, data[idx:idx+N])); idx += N
        E = list(map(int, data[idx:idx+M])); idx += M

        sumC = sum(C)
        sumE = sum(E)

        cnt = 0
        for x in C:
            if x * N < sumC and x * M > sumE:
                cnt += 1

        out.append(str(cnt))

    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()
