for _ in[0]*int(input()):
    p,q,r=input().split()
    a,b,c=map(int,p.split(':'))
    t=a*3600+b*60+c+1
    a,b,c=map(int,q.split(':'))
    t-=a*3600+b*60+c
    t*=-1
    t%=86400
    t-=int(r)*60-1
    if t>=0:print('Perfect')
    elif t>-3601:print('Test')
    else:print('Fail')