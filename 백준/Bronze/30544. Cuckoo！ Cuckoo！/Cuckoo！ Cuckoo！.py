p,q=map(int,input().split(':'))
n=int(input())
t=60*p+q
while n:
    if t%60 in[15,30,45]:
        n-=1
    if t%60==0:
        n=max(0,n-(t//60%12 or 12))
    t+=1
print(f'{t//60%12 or 12:02d}:{t%60-1:02d}')