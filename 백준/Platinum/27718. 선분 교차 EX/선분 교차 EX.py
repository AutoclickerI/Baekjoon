import sys
input=sys.stdin.readline
ccw=lambda *l:sum(l[i][1]*l[i-1][0]-l[i][0]*l[i-1][1]for i in range(len(l)))/2
def func(x1,y1,x2,y2,x3,y3,x4,y4):
    P,Q,R,S=ccw([x1,y1],[x2,y2],[x3,y3]),ccw([x1,y1],[x2,y2],[x4,y4]),ccw([x1,y1],[x3,y3],[x4,y4]),ccw([x2,y2],[x3,y3],[x4,y4])
    p,q=P*Q,R*S
    if p>0 or q>0:
        n=0
    elif p!=0!=q:
        n=1
    elif p+q:
        n=(p+q<0)*3
    else:
        a,b=sorted([(x1,y1),(x2,y2)]),sorted([(x3,y3),(x4,y4)])
        L=sorted(a+b)
        n=(a+b!=L!=b+a or len(set(a+b))!=4)*2
    if n==1:
        return 2
    elif n==2:
        if a+b==L or b+a==L or ((P or Q)and(R or S)):
            if L[0]==L[1] or L[1]==L[2] or L[2]==L[3]:return 1
        return 3
    elif n==3:
        return 1
    else:
        return 0
n=int(input())
l=[[*map(int,input().split())]for _ in[0]*n]
b=[[0]*n for _ in[0]*n]
for i in range(n-1):
    for j in range(i+1,n):
        b[i][j]=b[j][i]=func(*l[i],*l[j])
for i in range(n):b[i][i]=3
for i in b:
    print(*i,sep='')