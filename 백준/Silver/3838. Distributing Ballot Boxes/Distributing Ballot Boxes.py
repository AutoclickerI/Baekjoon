import sys
input=sys.stdin.readline
def possible(x):
    s=0;t=1
    for i in range(n):
        s+=((population[i]-1)//x+1)
        if s>b:t=0
    return t
while True:
    n,b=map(int,input().split())
    if n==-1:
        break
    population=[int(input()) for _ in range(n)]
    lo=0
    hi=10**8
    while(hi>lo+1):
        mi=(lo+hi)//2
        if possible(mi):
            hi=mi
        else:
            lo=mi
    print(hi)
    input()