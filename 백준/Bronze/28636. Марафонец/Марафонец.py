from datetime import*
ans=timedelta()
for _ in[0]*int(input()):
    p,q=map(int,input().split(':'))
    ans+=timedelta(minutes=p,seconds=q)
print(('0'+str(ans))[-8:])