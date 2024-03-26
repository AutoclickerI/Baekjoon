from itertools import*
n=int(input().split()[1])
for i,j in enumerate(product([*map(chr,range(97,123))],repeat=15)):
    if i==n:break
    print(''.join(j))