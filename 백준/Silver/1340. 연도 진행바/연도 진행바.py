from datetime import datetime

# 입력 읽기
s = input()
# 형식: "Month DD, YYYY HH:MM"
dt = datetime.strptime(s, "%B %d, %Y %H:%M")

year_start = datetime(dt.year, 1, 1, 0, 0)
year_end   = datetime(dt.year + 1, 1, 1, 0, 0)

elapsed = (dt - year_start).total_seconds()
total   = (year_end - year_start).total_seconds()
print(elapsed / total * 100)
