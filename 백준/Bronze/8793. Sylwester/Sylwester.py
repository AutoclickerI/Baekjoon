import sys
input=sys.stdin.readline
for _ in range(int(input())):
    N=int(input());a=n=0
    for _ in range(N):
        n+=int(input())
        if n<0:n+=1;a+=1
    print(abs(n)+a)