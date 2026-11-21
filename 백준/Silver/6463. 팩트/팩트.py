import math
for i in map(int,open(0)):print(f'{i:5d} ->',str(math.factorial(i)).strip('0')[-1])