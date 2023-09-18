N,_=map(int,input().split())
l=[]
for _ in[0]*N:
    l+=[*map(int,input().split())],
*s,=map(int,input().split())
m=[]
for i,j,k in l:
    tmp=[]
    for S in s:
        tmp+=[S//-j*-k,0][S<j],
    m+=100*i+sum(tmp),
for i in range(N):
    if min(m)==m[i]:exit(print(i+1))