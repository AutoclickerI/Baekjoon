s,N,K,R1,R2,C1,C2=map(int,input().split())
mg=N-K>>1

def recur(y,x,s):
    if s<1:
        return 0
    wh=N**(s-1)
    by=y//wh
    bx=x//wh
    if mg<=by<mg+K and mg<=bx<mg+K:
        return 1
    return recur(y%wh,x%wh,s-1)

for y in range(R1,R2+1):
    for x in range(C1,C2+1):
        print(recur(y,x,s),end='')
    print()