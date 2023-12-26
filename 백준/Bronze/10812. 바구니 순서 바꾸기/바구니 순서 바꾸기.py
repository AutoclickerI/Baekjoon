N,M=map(int,input().split())
*l,=range(1,N+1)
for _ in[0]*M:
    p,q,r=map(int,input().split())
    l[p-1:q]=l[r-1:q]+l[p-1:r-1]
print(*l)