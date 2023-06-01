import sys
input=sys.stdin.readline
l=[2**i for i in range(31)]
for _ in[0]*int(input()):print(+(int(input())in l))