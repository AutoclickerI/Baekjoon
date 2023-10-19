import math
for _ in[0]*int(input()):
    n=math.factorial(int(input()))
    while n%10==0:n//=10
    print(n%10)