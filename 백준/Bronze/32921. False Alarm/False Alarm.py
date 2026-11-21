A=[3]*600
for i in[*open(0)][1:]:v=int(i[0])*60+int(i[2:]);exec('A[v]-=A[v]>0;v+=1;'*11)
print(min(A))