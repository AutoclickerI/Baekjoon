from collections import Counter
import sys
a = []
for i in range(int(input())):
    a.append(int(sys.stdin.readline()))
a.sort()
print(round(sum(a)/len(a)))
print(a[len(a)//2])
b = Counter(a).most_common(n = 2)
try:
    if b[0][1] == b[1][1]:
        print(b[1][0])
    else:
        print(b[0][0])
except:
    print(a[0])
try:
    print(a[-1] - a[0])
except:
    print(0)
