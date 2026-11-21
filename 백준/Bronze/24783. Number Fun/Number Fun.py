for _ in[0]*int(input()):
    p,q,r=map(int,input().split())
    if r in[p-q,q-p,p*q,q/p,p/q,p+q]:print('Possible')
    else:print('Impossible')