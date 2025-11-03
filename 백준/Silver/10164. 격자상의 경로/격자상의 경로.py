N,M,K=map(int,input().split())
import math
f=lambda w,h:math.comb(w+h-2,w-1)
if K<1:
    print(f(N,M))
else:
    K-=1
    y,x=K//M,K%M
    print(f(y+1,x+1)*f(N-y,M-x))