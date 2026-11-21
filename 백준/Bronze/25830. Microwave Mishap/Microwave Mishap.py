p,q=map(int,input().split(':'))
t=p*3540+q*59
print(f'{t//3600:02d}:{t//60%60:02d}:{t%60:02d}')