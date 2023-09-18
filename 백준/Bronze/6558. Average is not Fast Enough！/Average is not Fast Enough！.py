from decimal import*
n,d=map(D:=Decimal,input().split())
while 1:
    try:
        a,*l=input().split()
        try:
            s=0
            for i in l:
                p,q,r=map(D,i.split(':'))
                s+=p*3600+q*60+r
            s=round(s/d+D(1)/10**10)
            print(f'{int(a):3}: {s//60}:{s%60:02} min/km')
        except:
            print(f'{int(a):3}: -')
    except:
        break
    