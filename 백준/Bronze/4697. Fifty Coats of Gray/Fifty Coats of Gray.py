import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n, width, length, height, area_per_can, m = map(int, line.split())
        if n == width == length == height == area_per_can == m == 0:
            break

        # 한 방당 칠해야 할 면적 = 벽 4면 + 천장
        # 벽 면적: 2 * (width * height) + 2 * (length * height)
        # 천장 면적: width * length
        wall_area = 2 * (width * height) + 2 * (length * height)
        ceiling_area = width * length
        total_room_area = wall_area + ceiling_area

        # 창문/문 면적 빼기
        openings_area = 0
        for _ in range(m):
            w, h = map(int, sys.stdin.readline().split())
            openings_area += w * h

        paint_area_per_room = total_room_area - openings_area
        total_paint_area = paint_area_per_room * n

        # 캔 수는 올림 처리
        cans_needed = (total_paint_area + area_per_can - 1) // area_per_can
        print(cans_needed)

if __name__ == "__main__":
    main()
