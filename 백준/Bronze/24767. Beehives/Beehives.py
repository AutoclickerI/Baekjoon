while s:=input():
 {*s}=={*'0. '}<exit();d,N=map(eval,s.split());l=[[*map(eval,input().split())]for _ in[0]*N];a=b=0;R=[0]*N
 for i in range(N-1):
  for j in range(i+1,N):t=(l[i][0]-l[j][0])**2+(l[i][1]-l[j][1])**2<d*d;R[i]|=t;R[j]|=t
 print(a:=sum(R),'sour,',N-a,'sweet')