_,W,*A=map(int,open(s:=0).read().split())
while W:s-=A[W:=W-1]-min(max(A[:W+1]),max(A[W:]))
print(s)