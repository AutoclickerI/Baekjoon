import sys
input=sys.stdin.readline

N,S,E=map(int,input().split())
dps=0
for _ in[0]*N:
    r,a,d=map(int,input().split())
    start=S//(r+a)
    end=((E-1)//(r+a)+1)
    dps+=d*(end-start)
    start*=r+a
    end*=r+a
    dps-=max(0,S-start-r)*d/a
    dps-=min(a,end-E)*d/a
print(dps/(E-S))