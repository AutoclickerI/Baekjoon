a, v, n, w = map(int, input().split())

ans = []
for i in range(n) : 
    for j in range(n) : 
        if a*i + v*j == w and i+j == n : 
            ans.append((i,j))
if len(ans) == 1 : 
    print(*ans[0])
else:
    print(-1)