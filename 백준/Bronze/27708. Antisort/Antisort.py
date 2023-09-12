print(n:=int(input()))
for _ in[0]*n:
    print(input())
    print(input())
    l=sorted(map(int,input().split()))
    print(*l[1:],l[0])