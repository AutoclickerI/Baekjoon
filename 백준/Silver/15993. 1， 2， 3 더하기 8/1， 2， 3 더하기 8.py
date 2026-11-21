m=10**9+9
l=[[0,0]for _ in[0]*100001]
l[0][1]=1
for i in range(1,100001):
    l[i]=(l[i-1][1]+l[i-2][1]+l[i-3][1])%m,(l[i-1][0]+l[i-2][0]+l[i-3][0])%m
for i in[*open(0)][1:]:print(*l[int(i)])