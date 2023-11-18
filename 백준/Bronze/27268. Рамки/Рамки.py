W,H,n=map(int,input().split())
l=[H*['.']for _ in[0]*W]
for i in range(n):
    a,b,c,d=map(int,input().split())
    l[c-1][b-1:d]=l[a-1][b-1:d]=[chr(97+i)]*(d-b+1)
    for j in range(a-1,c):
        l[j][b-1]=l[j][d-1]=chr(97+i)
for i in l:print(''.join(i))