[N,M],*l=[map(int,i.split())for i in open(0)]
A=[0]*N
for x,y in l:A[x-1]|=1<<y
print(sum((c:=(x&y).bit_count())*~-c//2for i,x in enumerate(A)for y in A[i+1:]))