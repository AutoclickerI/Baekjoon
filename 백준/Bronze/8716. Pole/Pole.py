import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    # 첫 번째 직사각형: (x1, y1)=왼쪽 상단, (x2, y2)=오른쪽 하단
    x1, y1, x2, y2 = data[0:4]
    # 두 번째 직사각형
    x3, y3, x4, y4 = data[4:8]

    # 가로 겹치는 길이
    overlap_w = max(0, min(x2, x4) - max(x1, x3))
    # 세로 겹치는 길이 (y축은 위쪽이 큰 값)
    overlap_h = max(0, min(y1, y3) - max(y2, y4))

    # 넓이
    area = overlap_w * overlap_h
    print(area)

if __name__ == "__main__":
    main()
