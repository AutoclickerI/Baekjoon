s=[{(0,0)}]
for _ in[0]*int(input()):
    x1,y1,x2,y2=map(int,input().split())
    tmp={(i,y1)for i in range(x1,x2+1)}|{(i,y2)for i in range(x1,x2+1)}|{(x1,i)for i in range(y1,y2+1)}|{(x2,i)for i in range(y1,y2+1)}
    ns=[]
    for i in s:
        if i&tmp:
            tmp|=i
        else:
            ns+=i,
    ns+=tmp,
    s=ns
print(len(s)-1)