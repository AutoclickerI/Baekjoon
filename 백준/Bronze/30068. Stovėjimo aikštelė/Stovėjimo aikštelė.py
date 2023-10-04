d={}
cnt={}
ans=[]
for _ in[0]*int(input()):
    p,q=map(int,input().split())
    if cnt.get(q,0)%2:
        cnt[q]+=1
        d[q]+=p
        ans+=q,
    else:
        cnt[q]=cnt.get(q,0)+1
        d[q]=d.get(q,0)-p
        if q in ans:
            ans.pop(ans.index(q))
for i in ans:
    print(i,d[i])