from functools import cache

N,L,R=map(int,input().split())

@cache
def get(N,L,R):
    if N==1:
        return L==R==1
    if L<1 or R<1:
        return 0
    return(get(N-1,L-1,R)+get(N-1,L,R-1)+get(N-1,L,R)*(N-2))%(10**9+7)

print(+get(N,L,R))