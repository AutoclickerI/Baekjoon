from itertools import*
print(sum(all(2**.5/i[7-j]<1/i[-j]+1/i[6-j]for j in range(8))for i in permutations(map(int,input().split()))))