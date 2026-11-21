import sys
input=sys.stdin.readline
p,q=map(eval,input().split())
l=[p/q,q/p]
for _ in[0]*int(input()):
    p,q=input().split()
    print(eval(p)*l[q=='A'])