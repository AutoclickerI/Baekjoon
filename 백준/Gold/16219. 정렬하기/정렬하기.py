import sys
input=sys.stdin.readline
N=int(input())
*l,=map(int,input().split())
S=sorted(l)
M=int(input())
if N==1:
    print(*[0]*M)
else:
    for _ in[0]*M:
        p,q=map(int,input().split())
        l[p],l[q]=l[q],l[p]
        print((l!=S)*(2*(N==2)-1),end=' ')