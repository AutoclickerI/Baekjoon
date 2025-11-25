N,M,K=map(int,input().split())
b=[M*[0]for _ in[0]*N]
s=[]
for _ in[0]*K:
    R,C=map(int,input().split())
    s+=[[*map(int,input().split())]for _ in[0]*R],

def check(y,x,arr):
    for dy in range(len(arr)):
        for dx in range(len(arr[0])):
            if arr[dy][dx]==b[y+dy][x+dx]==1:
                return 0
    for dy in range(len(arr)):
        for dx in range(len(arr[0])):
            b[y+dy][x+dx]+=arr[dy][dx]
    return 1
def put(arr):
    for y in range(N-len(arr)+1):
        for x in range(M-len(arr[0])+1):
            if check(y,x,arr):
                return 1

for i in s:
    for _ in[0]*4:
        if put(i):
            break
        i=[j[::-1]for j in zip(*i)]

print(sum(sum(i)for i in b))