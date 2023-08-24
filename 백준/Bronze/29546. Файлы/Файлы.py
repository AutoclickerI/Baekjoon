f=[input()for _ in[0]*int(input())]
for _ in[0]*int(input()):
    p,q=map(int,input().split())
    print(*f[p-1:q])