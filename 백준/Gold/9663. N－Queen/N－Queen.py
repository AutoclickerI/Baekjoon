N=int(input())
queens=[-1]*N

def check(i):
    for j in range(i):
        if abs(queens[i]-queens[j])==i-j or queens[i]==queens[j]:
            return 0
    return 1

ans=0
def backtrack(n):
    global ans
    if n==N:
        ans+=1
        return
    for i in range(N):
        queens[n]=i
        if check(n):
            backtrack(n+1)
backtrack(0)
print(ans)