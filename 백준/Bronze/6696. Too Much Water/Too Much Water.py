import math
import sys

for line in sys.stdin:
    x, y = map(float, line.split())
    if x == 0 and y == 0:
        break
    d2 = x*x + y*y
    hours = math.ceil(math.pi * d2 / 100.0)
    print(f"The property will be flooded in hour {hours}.")
