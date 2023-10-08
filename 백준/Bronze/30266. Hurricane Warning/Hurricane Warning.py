import sys
input=sys.stdin.readline
for i in range(int(input())):
    n=int(input())
    s=input()
    cnt=0
    for _ in[0]*n:
        cnt+=any(i in s for i in input()[:-1])
    print(f'Data Set {i+1}:')
    print(cnt)
    print()