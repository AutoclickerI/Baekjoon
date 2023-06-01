a,b,x,y=map(int,input().split())
A=abs
print(min(A(a-b),A(a-x)+A(b-y),A(a-y)+A(b-x)))