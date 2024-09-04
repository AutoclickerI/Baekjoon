def ask(l,Q='?'):print(Q,''.join('RSP'[i]for i in l))
N=int(input())
ask(l:=[0]*N)
p,q,r=map(int,input().split())
if 418<N-p:
    ask(l:=[1]*N)
    p,q,r=map(int,input().split())
    if 417<N-p:
        ask(l:=[2]*N)
        p,q,r=map(int,input().split())

while q+r+2:
    if r<0 or 0<q<r:
        l[q-1]=(l[q-1]+2)%3
    else:
        l[r-1]=(l[r-1]+1)%3
    ask(l)
    p,q,r=map(int,input().split())
ask(l,'!')