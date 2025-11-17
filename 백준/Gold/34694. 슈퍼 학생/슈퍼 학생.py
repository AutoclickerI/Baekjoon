a,b,w,M=map(int,input().split())
F=sorted(int(input())for _ in[0]*a)[::-1]+[0]*(M-b-1)
S=sorted(max(map(int,input().split()))for _ in[0]*w)
v=0
for i in zip(*[iter(F)]*(M-b)):v+=~-max(S.pop(),max(i))
print(v+sum(S)-len(S)<<1)