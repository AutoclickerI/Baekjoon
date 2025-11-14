N=int(input())
l=list(map(int,input().split()))
stack=[]
ans=[]
while l:
    v=l.pop()
    while stack and stack[-1]<=v:
        stack.pop()
    if stack:
        ans.append(stack[-1])
    else:
        ans.append(-1)
    stack.append(v)
ans.reverse()
print(*ans)