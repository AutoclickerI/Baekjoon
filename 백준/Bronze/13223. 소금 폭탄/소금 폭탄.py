p=input()
q=input()
if p==q:print('24:00:00')
else:
    a,b,c=map(int,p.split(':'))
    n=3600*a+60*b+c
    a,b,c=map(int,q.split(':'))
    n=3600*a+60*b+c-n
    n%=86400
    print(f'{n//3600:02d}:{n//60%60:02d}:{n%60:02d}')