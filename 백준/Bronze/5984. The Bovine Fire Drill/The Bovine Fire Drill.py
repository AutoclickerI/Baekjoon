N,A=int(input()),1
T,*C=range(1+N)
while C[x:=(A+T)%N]-1==x>0:C[x],T,A=A,x,C[x]
print(A)