p,q,r=map(int,input().split())
l=[0]+[0]*p
l[q]=1
exec('p,q=map(int,input().split());l[p],l[q]=l[q],l[p];'*r)
print(l.index(1))