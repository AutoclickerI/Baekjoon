*l,m=sorted(map(int,[*open(0)][1].split()))
from collections import deque
a=deque([m])
for i in l[::-1]:
    if a[0]*i>a[-1]*i:
        a.appendleft(i)
    else:
        a.append(i)
a=[*a]
print(sum(i*j for i,j in zip(a,a[1:]+[a[0]])))
print(*a)