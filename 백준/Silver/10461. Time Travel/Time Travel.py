import sys
from fractions import Fraction

# 상수 정의 (정수)
SECS_IN_12_HOURS = 43200
SECS_IN_A_DAY = 86400
MINS_IN_12_HOURS = 720

try:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        a, b = map(int, line.split())

        # 시간 차이가 벌어지는 속도
        diff_rate = abs(a - b)
        
        # 부동소수점 오차를 피하기 위해 모든 계산을 Fraction으로 수행
        # Jim의 시계가 표시하는 총 시간(초)을 분수로 계산
        total_watch_seconds_frac = Fraction(SECS_IN_12_HOURS * (SECS_IN_A_DAY - a), diff_rate)
        
        # 12시간 주기로 변환
        seconds_on_face_frac = total_watch_seconds_frac % SECS_IN_12_HOURS
        
        # 분으로 변환
        total_minutes_on_face_frac = seconds_on_face_frac / 60
        
        # 반올림: 0.5 (Fraction(1, 2))를 더하고 정수 부분만 취함
        rounded_total_minutes = int(total_minutes_on_face_frac + Fraction(1, 2))
        
        # 12시간(720분) 주기로 변환
        final_minute_in_cycle = rounded_total_minutes % MINS_IN_12_HOURS
        
        # 시간(HH)과 분(MM)으로 변환
        hour = final_minute_in_cycle // 60
        minute = final_minute_in_cycle % 60
        
        # 0시는 12시로 표시
        if hour == 0:
            hour = 12
            
        # 형식에 맞춰 출력
        print(f"{a} {b} {hour:02d}:{minute:02d}")

except (IOError, ValueError):
    pass