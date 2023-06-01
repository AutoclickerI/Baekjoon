import math
b,a=list(map(int,input().split()));print(int(math.factorial(b)//(math.factorial(a)*math.factorial(b-a)))%10007)