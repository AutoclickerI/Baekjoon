N,*l=map(int,open(0).read().split())

x=0
r=[[]for _ in[0]*N.bit_length()]

def recur(i,y):
    global x,r
    if N<i:
        return
    recur(i<<1,y+1)
    r[y]+=(l[i-1],x),
    x+=1
    recur(i<<1|1,y+1)

recur(1,0)

def kadane(arr):
    v=0
    return max(v:=i+max(v,0)for i in arr)

rr=-float('inf')
for i in range(len(r)):
    arr=[0]*N
    f=[0]*N
    for j in range(i,len(r)):
        for v,x in r[j]:
            arr[x]=v
            f[x]=1
        rr=max(rr,kadane([i for i,j in zip(arr,f)if j]))
print(rr)