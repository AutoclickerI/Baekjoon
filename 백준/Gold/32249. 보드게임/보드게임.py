import sys
input=sys.stdin.readline
N,M=map(int,input().split())
Alice=[[*input()]for _ in[0]*N]
Bob=[[*input()]for _ in[0]*N]
AcntB=sum(i=='B'for j in Alice for i in j)
sB={i for i in range(M)if Alice[-1][i]=='B'}
BcntA=sum(i=='A'for j in Bob for i in j)
sA={i for i in range(M)if Bob[-1][i]=='A'}
def check_cond():
    Aturn=1+(AcntB-bool(sB))*2
    Bturn=(1+BcntA-bool(sA))*2
    print(['Bob','Alice'][Aturn<Bturn])
check_cond()
Q=int(input())
for _ in[0]*Q:
    r1,c1,r2,c2=map(int,input().split())
    achange=Alice[r1-1][c1-1]
    bchange=Bob[r2-1][c2-1]
    if achange!=bchange:
        Bob[r2-1][c2-1]=achange
        Alice[r1-1][c1-1]=bchange
        if achange=='B':
            AcntB-=1
            if r1==N:
                sB.remove(c1-1)
            BcntA-=1
            if r2==N:
                sA.remove(c2-1)
        else:
            BcntA+=1
            if r2==N:
                sA.add(c2-1)
            AcntB+=1
            if r1==N:
                sB.add(c1-1)
    check_cond()