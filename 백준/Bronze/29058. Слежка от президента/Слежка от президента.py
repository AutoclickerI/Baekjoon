i,*l=open(0)
N,M,K=map(int,i.split())
A=[c:='']*N
n=0
for i,*_ in l:
  if i=='N':n=-~n%N
  elif i=='C':c=A[n][-K:]
  elif i=='P':A[n]+=c
  elif i=='B':A[n]=A[n][:-1]
  else:A[n]+=i
print(A[n][-K:]or'Empty')