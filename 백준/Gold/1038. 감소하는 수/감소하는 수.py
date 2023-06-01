from itertools import*
try:print(sorted(map(int,[''.join(i)for j in range(10)for i in combinations('9876543210',j+1)]))
[int(input())])
except:print(-1)