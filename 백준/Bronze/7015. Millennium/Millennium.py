import sys

def days_in_year(year):
    # 연도가 3의 배수인 경우 10개의 대월(20일)
    if year % 3 == 0:
        return 10 * 20
    # 그렇지 않으면 대월과 소월이 번갈아, 대월 5개(20일) + 소월 5개(19일)
    return 5 * 20 + 5 * 19

def days_in_month(year, month):
    # 3의 배수해인 경우 모든 월이 대월(20일)
    if year % 3 == 0:
        return 20
    # 그렇지 않으면 홀수월 대월(20일), 짝수월 소월(19일)
    return 20 if month % 2 == 1 else 19

def serial_day(year, month, day):
    # 시작일(1/1/1)부터 해당일까지의 누적 일수
    total = 0
    for y in range(1, year):
        total += days_in_year(y)
    for m in range(1, month):
        total += days_in_month(year, m)
    total += day
    return total

def calculate_durations(inputs):
    # 기준 날짜: 1000년 1월 1일
    target_serial = serial_day(1000, 1, 1)
    results = []
    for y, m, d in inputs:
        birth_serial = serial_day(y, m, d)
        results.append(target_serial - birth_serial)
    return results

data = open(0).read().strip().split()
n = int(data[0])
coords = list(map(int, data[1:]))
inputs = [(coords[i], coords[i+1], coords[i+2]) for i in range(0, len(coords), 3)]

outputs = calculate_durations(inputs)
# 결과 출력
print("\n".join(map(str, outputs)))
