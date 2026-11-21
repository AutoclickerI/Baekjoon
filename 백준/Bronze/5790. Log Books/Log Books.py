import sys

def time_to_minutes(time_str):
    """ HH:MM 형식의 시간을 분으로 변환 """
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes

def is_night_time(start, end, sunrise, sunset):
    """ 야간 시간 (해 뜨기 전 또는 해 진 후) 계산 """
    night_minutes = 0

    # 운전이 야간에 얼마나 걸치는지 확인
    if start < sunrise:  # 해 뜨기 전 운전한 부분
        night_minutes += min(end, sunrise) - start
    if end > sunset:  # 해 진 후 운전한 부분
        night_minutes += end - max(start, sunset)

    # 만약 총 운전 시간의 절반 이상이 야간이면 전체 시간을 야간으로 포함
    return night_minutes >= (end - start) / 2

def process_log_book(entries):
    total_minutes = 0  # 총 운전 시간
    night_minutes = 0  # 야간 운전 시간

    for entry in entries:
        sunrise, sunset, start, end = map(time_to_minutes, entry.split())

        drive_time = end - start
        if drive_time > 120:  # 단일 운전 기록이 2시간 초과면 "NON"
            return "NON"

        total_minutes += drive_time
        if is_night_time(start, end, sunrise, sunset):
            night_minutes += drive_time

    # 최소 50시간(3000분) & 최소 10시간(600분) 야간 운전 필요
    return "PASS" if total_minutes >= 3000 and night_minutes >= 600 else "NON"

def solve():
    input_data = sys.stdin.read().splitlines()
    index = 0
    results = []

    while index < len(input_data):
        n = int(input_data[index])  # 첫 번째 줄: 기록 개수
        if n == 0:
            break  # 0이면 입력 종료
        entries = input_data[index + 1 : index + 1 + n]  # 다음 n개의 줄이 운전 기록
        results.append(process_log_book(entries))  # 결과 저장
        index += n + 1  # 다음 테스트 케이스로 이동

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()