import math
print(min(int(i[:4])+math.lcm(int(i[4:7]),int(i[7:]))for i in[*open(0)][1:]))