n=int(input())
l=[tuple(map(int,input().split()))for _ in[0]*n]
for i in range(n):
    if l[i][i]:print(1);exit()
for i in range(n):
    for j in range(n):
        if l[i][j]<1 and i-j:print(2);exit()
if l!=[*zip(*l)]:print(3);exit()
for i in range(n):
    for j in range(n):
        for k in range(n):
            if l[i][j]+l[j][k]<l[i][k]:print(4);exit()
print(0)