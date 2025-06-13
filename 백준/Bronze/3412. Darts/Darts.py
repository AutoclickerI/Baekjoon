import sys
input=sys.stdin.readline
for _ in[0]*int(input()):
    a=0
    for _ in[0]*int(input()):
        i,j=map(int,input().split())
        v=i*i+j*j
        for i in range(10,0,-1):
            if v<=i*i*400:
                a+=1
    print(a)