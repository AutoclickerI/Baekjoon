N,K,*A=map(int,open(0).read().split())
tmp=[0,0]*N
cnt=[0]
flag=[1]
def merge_sort(p,r):
 if p<r:q=(p+r)//2;merge_sort(p,q);merge_sort(q+1,r);merge(p,q,r)
def merge(p,q,r):
 i,j,t=p,q+1,1
 while i<=q and j<=r:
  if A[i]<=A[j]:tmp[t]=A[i];i+=1
  else:tmp[t]=A[j];j+=1
  t+=1
 while i<=q:tmp[t]=A[i];t+=1;i+=1
 while j<=r:tmp[t]=A[j];t+=1;j+=1
 i,t=p,1
 while i<=r:
  A[i]=tmp[t];t+=1;i+=1;cnt[0]+=1
  if K==cnt[0]:print(A[i-1]);flag[0]=0
merge_sort(0,N-1)
if flag[0]:print(-1)