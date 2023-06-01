import math
while int((l:=input())):print(sum(int(l[::-1][i])*math.factorial(i+1)for i in range(len(l))))