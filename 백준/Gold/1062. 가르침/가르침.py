from itertools import*
import sys
input=lambda:sys.stdin.readline().strip()

def f(i):
    i={*i}
    return sum(j<=i for j in l)

N,K=map(int,input().split())
K-=5
l=[{*input()}-{*'antic'}for _ in[0]*N]
if K<0:
    print(0)
else:
    print(max(f(i)for i in combinations('bdefghjklmopqrsuvwxyz',K)))