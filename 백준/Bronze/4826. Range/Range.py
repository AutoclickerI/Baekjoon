f=lambda:[*map(eval,input().split())]
while(l:=f())[0]>0:
    t=[l];k=u=0
    while(l:=f())[0]>0:t+=l,
    for v,w in zip(t,t[1:]):
        a,b=v;c,d=w
        if b>d:u+=c-a;k+=b-d
    print(round(u/k*d))