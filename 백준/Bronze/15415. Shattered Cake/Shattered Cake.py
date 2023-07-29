import sys
input=sys.stdin.readline
W=int(input())
L=int(input())
a=0
for _ in[0]*L:
    p,q=map(int,input().split())
    a+=p*q
print(a//W)