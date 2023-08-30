a,b=map(int,input().split(':'))
c,d=map(int,input().split(':'))
t=((c-a+24)*60+d-b)
print(f'{t//60:02}:{t%60:02}')