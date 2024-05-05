N,s,M=map(int,input().split())
ans=0,0,0
for i in range(1,13):
 N1=i+10;N2=s;cnt=0
 for N3 in range(1,N+1):
  if (N3<10 or 10<N3<23):continue
  five=N1*1000+N2*100+N3%100
  if five%(N1+N2)<1 or five%(N2+N3)<1 or five%(N3+N1)<1:
   cnt+=1
   if i==M>0==ans[0]:ans=N1,N2,N3
 print(cnt)
print(*ans)