while s:=input():
 {*s}=={*'0. '}<exit();d,N=map(eval,s.split());l=[eval(input().replace(' ','+1j*'))for _ in[0]*N];a=b=0;R=[0]*N
 for i in range(N):
  for j in range(i+1,N):t=abs(l[i]-l[j])<d;R[i]|=t;R[j]|=t
 print(a:=sum(R),'sour,',N-a,'sweet')