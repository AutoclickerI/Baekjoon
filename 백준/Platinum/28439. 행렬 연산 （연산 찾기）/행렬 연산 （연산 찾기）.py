I=iter(open(0))
N,M=map(int,next(I).split())
N=range(N)
M=range(M)
arr=[[*map(int,next(I).split())]for _ in N]
R=[arr[i][0]for i in N]
C=[arr[0][0]-arr[0][i]for i in M]
from collections import*
if[[R[i]-C[j]for j in M]for i in N]!=arr:
    print(-1)
else:
    most=Counter(R+C).most_common()[0][0]
    ansbox=[]
    for i in N:
        if R[i]-most:ansbox+=(1,i+1,R[i]-most),
    for i in M:
        if C[i]-most:ansbox+=(2,i+1,most-C[i]),
    print(len(ansbox))
    for i in ansbox:print(*i)