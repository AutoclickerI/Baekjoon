p,q,r=map(int,input().split())
l=[0]+[0]*p
l[q]=1
for _ in[0]*r:
    p,q=map(int,input().split())
    l[p],l[q]=l[q],l[p]
print(l.index(1))