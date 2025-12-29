def backtrack(arr,v):
    global m
    n=len(arr)
    if 10<n:
        m=max(m,v)
        return
    for i in range(11):
        if b[n][i] and i not in arr:
            arr+=i,
            backtrack(arr,v+b[n][i])
            arr.pop()
for _ in[0]*int(input()):
    m=0
    b=[[*map(int,input().split())]for _ in[0]*11]
    backtrack([],0)
    print(m)