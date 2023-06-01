import math
for i in range(int(input())):a,b=list(map(int,input().split()));print(int(math.factorial(b)/(math.factorial(a)*math.factorial(b-a))))