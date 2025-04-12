import math
for i in open(0).read().split()[:-1]:
    f=str(math.factorial(int(i))).count
    print(f'{i}!','--')
    print(*[f'   ({j}){f(str(j)):5}'for j in range(5)])
    print(*[f'   ({j}){f(str(j)):5}'for j in range(5,10)])