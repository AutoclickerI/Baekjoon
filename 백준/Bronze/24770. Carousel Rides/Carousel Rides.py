*l,_=open(0)
while l:
    n,m,*t=map(int,l.pop(0).split())
    for _ in[0]*n:
        a,b=map(int,l.pop(0).split())
        if a<=m:
            t+=(a,b),
    if t:
        a,b=min(t,key=lambda x: (int(x[1])/int(x[0]),-int(x[0])))
        print(f'Buy {a} tickets for ${b}')
    else:
        print('No suitable tickets offered')