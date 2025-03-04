N=int(input())
*A,=map(eval,input().split())
for i in range(N):A[i]=int(A[i]*100+.5)
x,Q=map(int,input().split())
x-=1
s=sum(A)-A[x]
c=N-1
ans=A[x]
for _ in range(Q):
  a,b=input().split()
  if a=="O":b=int(b)-1;s-=A[b];c-=1
  else:
    if b=="N":continue
    ans=s/c*0.9
    break

print(f'{A[x]/100:.2f} {ans/100:.2f}')