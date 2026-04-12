N,M=map(int,input().split())
sl=[]
for _ in[0]*N:
    p,q=map(int,input().split())
    sl+=[q]*p
rl=[]
for _ in[0]*M:
    p,q=map(int,input().split())
    rl+=[q]*p
print(max(0,*[j-i for i,j in zip(sl,rl)]))