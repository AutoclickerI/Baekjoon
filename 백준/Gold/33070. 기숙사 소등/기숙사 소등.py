from bisect import*
N,K=map(int,input().split())
A=sorted(map(int,input().split()))

*l,=map(int,input().split())
cl=cnt=0
for i in range(N):
    if l[i]:
        idx=bisect_left(A,cnt)
        if idx<K:
            cl+=cnt<=A[idx]<=cnt+cl
    cnt+=l[i]<1
print(N-cnt-cl)