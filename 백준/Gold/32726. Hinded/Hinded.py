[N],*b=[[*map(int,i.split())]for i in open(0)]
b=[[50-j for j in i]for i in b]

def kadane(arr):
    v=0
    return max(v:=i+max(v,0)for i in arr)

r=0
for i in range(N):
    arr=[0]*N
    for j in range(i,N):
        *arr,=map(int.__add__,arr,b[j])
        r=max(r,kadane(arr))
print(r-sum(sum(b,[])))