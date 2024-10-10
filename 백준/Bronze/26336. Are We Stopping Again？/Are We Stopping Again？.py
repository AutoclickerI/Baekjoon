import math

def calculate_stops(total_miles, gas_interval, food_interval):
    # 주유 정차 횟수
    gas_stops = (total_miles - 1) // gas_interval
    # 식사 정차 횟수
    food_stops = (total_miles - 1) // food_interval
    # 겹치는 정차 횟수 (주유와 식사 모두 해당)
    overlap_stops = (total_miles - 1) // math.lcm(gas_interval, food_interval)
    
    # 총 정차 횟수 = 주유 정차 + 식사 정차 - 겹치는 정차
    total_stops = gas_stops + food_stops - overlap_stops
    return total_stops

# 입력 받기
t = int(input())
for _ in range(t):
    total_miles, gas_interval, food_interval = map(int, input().split())
    
    # 정차 횟수 계산
    stops = calculate_stops(total_miles, gas_interval, food_interval)
    
    # 결과 출력
    print(f"{total_miles} {gas_interval} {food_interval}")
    print(stops)