A,B=input().split()
from itertools import*
l=[-1]
for i in permutations(A):
    v=int(''.join(i))
    if'0'!=i[0]and v<int(B):
        l+=v,
print(max(l))