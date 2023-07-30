import sys
input=sys.stdin.readline
for _ in[0]*int(input()):
    p,q=map(int,input().split())
    c=0
    while p<q:c+=1;p*=2
    print(c)