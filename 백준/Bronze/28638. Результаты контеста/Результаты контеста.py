ans=[0,0]
d={}
for _ in[0]*int(input()):
    p,q,r=input().split()
    p,P=map(int,p.split(':'))
    t=p*60+P
    if r=='CE':
        continue
    elif r=='OK':
        if not d.get(q,[0,0])[0]:
            tmp=d.get(q,[0,0])
            tmp[0]=1
            tmp[1]+=t
            ans[0]+=1
            ans[1]+=tmp[1]
            d[q]=tmp
    else:
        if not d.get(q,[0,0])[0]:
            tmp=d.get(q,[0,0])
            tmp[1]+=20
            d[q]=tmp
print(*ans)