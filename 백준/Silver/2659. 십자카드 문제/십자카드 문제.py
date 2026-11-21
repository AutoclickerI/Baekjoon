def getn(arr):
    arr*=2
    return min(int(''.join(arr[i:i+4]))for i in range(4))

r=[]
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            for l in range(1,10):
                r+=getn([*map(str,[i,j,k,l])]),
r=sorted({*r})
n=getn(input().split())
print(r.index(n)+1)