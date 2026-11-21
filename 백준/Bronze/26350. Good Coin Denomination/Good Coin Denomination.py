for i in[*open(0)][1:]:
    p,v,*q=map(int,i.split())
    print('Denominations:',v,*q)
    while q:
        x=q.pop(0)
        if 2*v>x:print('Bad coin denominations!\n');break
        v=x
    else:print('Good coin denominations!\n')