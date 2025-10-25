N,R=map(int,input().split())
b=[[*map(int,input().split())]for _ in[0]*2**N]
rot=[[[1,2],[3,4]]for _ in[0]*N]

def split(arr,n):
    r=2**n
    return[[[[*k][j:j+r]for k in i]for j in range(0,2**N,r)]for i in zip(*[iter(arr)]*r)]

def merge(arr):
    ret=[]
    for i in arr:
        tmp=[[]for _ in[0]*len(i[0])]
        for j in i:
            for k in range(len(j)):
                tmp[k]+=j[k]
        ret+=tmp
    return ret

for _ in[0]*R:
    k,l=map(int,input().split())
    if k==1:
        for i in range(l):
            rot[i]=rot[i][::-1]
    if k==2:
        for i in range(l):
            rot[i]=[i[::-1]for i in rot[i]]
    if k==3:
        for i in range(l):
            rot[i]=[[*i][::-1]for i in zip(*rot[i])]
    if k==4:
        for i in range(l):
            rot[i]=[[*i]for i in zip(*[i[::-1]for i in rot[i]])]
    if k==5:
        for i in range(l,N):
            rot[i]=rot[i][::-1]
    if k==6:
        for i in range(l,N):
            rot[i]=[i[::-1]for i in rot[i]]
    if k==7:
        for i in range(l,N):
            rot[i]=[[*i][::-1]for i in zip(*rot[i])]
    if k==8:
        for i in range(l,N):
            rot[i]=[[*i]for i in zip(*[i[::-1]for i in rot[i]])]

org=[[[1,2],[3,4]]for _ in[0]*N]
i=N
while i:
    b=split(b,i)
    while sum(org[i-1][0])!=sum(rot[i-1][0]):
        for y in range(len(b)):
            for x in range(len(b)):
                b[y][x]=[[*i][::-1]for i in zip(*b[y][x])]
        for j in range(i):
            org[j]=[[*i][::-1]for i in zip(*org[j])]
    if org[i-1][0]!=rot[i-1][0]:
        for y in range(len(b)):
            for x in range(len(b)):
                b[y][x]=[i[::-1]for i in b[y][x]]
        for j in range(i):
            org[j]=[i[::-1]for i in org[j]]
    i-=1
    b=merge(b)
for i in b:print(*i)