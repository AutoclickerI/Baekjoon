p,q=map(int,input().split())
l=[*range(p+1)]
for _ in[0]*q:
    p,q=map(int,input().split())
    l[p],l[q]=l[q],l[p]
print(*l[1:])