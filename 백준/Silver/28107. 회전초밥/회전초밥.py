N,M=map(int,input().split())

l=[[]for _ in[0]*200001]
for v in range(N):
    for i in input().split()[1:]:
        l[int(i)]+=v,

l=[i[::-1]for i in l]
cnt=[0]*N

for i in map(int,input().split()):
    if l[i]:
        cnt[l[i].pop()]+=1
print(*cnt)