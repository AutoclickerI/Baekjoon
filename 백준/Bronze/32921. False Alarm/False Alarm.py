A=[3]*600
for i in[*open(0)][1:]:
 a,b=map(int,i.split(':'))
 for i in range(11):A[i+a*60+b]-=1
print(max(0,min(A)))