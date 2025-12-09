_,*A,S=map(int,open(0).read().split())
while A:i=A.index(max(A[:S+1]));S-=i;print(A.pop(i))