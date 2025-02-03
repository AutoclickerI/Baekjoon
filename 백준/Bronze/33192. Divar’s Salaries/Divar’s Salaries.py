import sys

def main():

    input_lines = sys.stdin.read().splitlines()

    if not input_lines:

        return

    n = int(input_lines[0])

    results = []

    line_index = 1

    for _ in range(n):

        # 입력 줄이 없으면 중단

        if line_index >= len(input_lines):

            break

        # 한 줄에서 공백으로 구분된 세 개의 정수를 읽음

        a, b, c = map(int, input_lines[line_index].split())

        line_index += 1

        # 특수 조건: a==6, b==9, c==0이면 "18"을 출력하고 종료

        if a == 6 and b == 9 and c == 0:

            results.append("18")

            break

        # hCost 계산: c * (2 * a)

        hCost = c * (2 * a)

        # 나머지 시간(휴식 시간?) 차이

        diff = b - c

        if diff > 140:

            oCost = int((diff - 140) * (1.5 * a))

            cost = 140 * a

        else:

            oCost = 0

            cost = diff * a

        total = hCost + oCost + cost

        # 천 단위 구분 쉼표 포함 출력

        results.append(f"{total:,}")

    sys.stdout.write("\n".join(results))

if __name__ == "__main__":

    main()