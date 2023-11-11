import sys
input=sys.stdin.readline
while(s:=input())>'00':
    n,m=map(int,s.split())
    print(*{str(i+1)for i in range(n)}-{str(m)}-{input()[:-1]for _ in[0]*(n-2)})