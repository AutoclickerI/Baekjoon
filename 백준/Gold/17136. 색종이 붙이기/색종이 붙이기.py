b=[[*map(int,i[::2])]for i in open(0)]
v=[5,5,5,5,5]
cnt=float('inf')
def check(y,x,c):
    for dy in range(c):
        for dx in range(c):
            if 9<y+dy or 9<x+dx or b[y+dy][x+dx]<1:
                return 0
    return 1

def apply(y,x,c):
    for dy in range(c):
        for dx in range(c):
            b[y+dy][x+dx]^=1

def backtracking(n):
    global cnt
    if n==100:
        cnt=min(cnt,25-sum(v))
        return
    y,x=n//10,n%10
    if b[y][x]<1:
        backtracking(n+1)
    else:
        for i in range(5):
            if v[i] and check(y,x,i+1):
                v[i]-=1
                apply(y,x,i+1)
                backtracking(n+1)
                apply(y,x,i+1)
                v[i]+=1
backtracking(0)
print(-(cnt==float('inf'))or cnt)