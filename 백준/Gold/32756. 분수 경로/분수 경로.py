N,D=map(int,input().split())
import math
gcd=math.gcd(abs(N),D)
N//=gcd
D//=gcd

s=''
while D>1:
    if D%2:
        exit(print(-1))
    D//=2
    s+='D'

i=-1
l=[]
if N<0:
    while N+2**i<0:
        i+=1
    N+=2**i

if -1<i:
    while N:
        if N%2:
            s+='R'
        N//=2
        s+='U'
        i-=1
    s+='U'*i
    s+='L'
else:
    while N:
        if N%2:
            s+='R'
        N//=2
        s+='U'
print(len(s))
print(s)