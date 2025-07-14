import sys

input = sys.stdin.readline

N=int(input())
*l,=map(int,input().split())

for _ in range(int(input())):
    Q,c,*x=map(int,input().split())
    if Q==1:
        x=x[0]
        right=left=x
        i=c-1
        while 0<=i:
            dv=min(left,l[i])
            l[i]+=dv
            left-=dv
            if dv<1:break
            i-=1
        while c<N:
            dv=min(right,l[c])
            l[c]+=dv
            right-=dv
            if dv<1:break
            c+=1
    else:
        print(l[c-1])