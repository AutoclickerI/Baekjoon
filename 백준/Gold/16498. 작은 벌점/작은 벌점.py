input()
l=[sorted(map(int,input().split()))for _ in[0]*3]
ptr=[0]*3
def increase_key(n):
    if ptr[n]<len(l[n])-1:
        ptr[n]+=1
        return True
    return False
m=1e9
f=True
while f:
    v,k=zip(*sorted((l[i][ptr[i]],i)for i in[0,1,2]))
    m=min(m,max(v)-min(v))
    f=False
    for i in k:
        if increase_key(i):
            f=True
            break
print(m)