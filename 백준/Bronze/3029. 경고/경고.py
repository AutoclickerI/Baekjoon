p,q,r=map(int,input().split(':'))
n=(p+24)*60*60+q*60+r
p,q,r=map(int,input().split(':'))
n=(p*60*60+q*60+r-n)%(60*60*24)
H=n//(60*60)
n%=(60*60)
M=n//60
n%=60
if H+M+n:
    print('{:02d}:{:02d}:{:02d}'.format(H,M,n))
else:
    print('24:00:00')