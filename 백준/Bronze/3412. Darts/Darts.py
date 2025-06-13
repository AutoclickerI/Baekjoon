import sys
input=sys.stdin.readline
for _ in[0]*int(input()):
    a=0
    for _ in[0]*int(input()):
        i,j=map(int,input().split())
        for k in range(1,11):a+=i*i+j*j<=k*k*400
    print(a)