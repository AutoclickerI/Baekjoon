_,W,*h=map(int,open(0).read().split())

stack = []
ans = 0

for i in range(W):
    while stack and h[stack[-1]]<h[i]:
        bottom = stack.pop()
        if not stack:
            break
        left = stack[-1]
        height = min(h[left], h[i]) - h[bottom]
        width = i - left - 1
        ans += height * width
    stack.append(i)

print(ans)