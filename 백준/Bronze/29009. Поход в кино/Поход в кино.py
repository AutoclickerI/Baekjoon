N,A,B=map(int,input().split())
x=N-2*A+1
y=N-2*B+1
if x>0 and y>0:
    print(x*y-1)
else:
    print(0)