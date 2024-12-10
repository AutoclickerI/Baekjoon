A=[3]*999
for a,_,b,c,_ in[*open(0,'rb')][1:]:
 for j in range(11):A[j+a*60+b*10-3360+c]-=1
print(max(0,min(A)))