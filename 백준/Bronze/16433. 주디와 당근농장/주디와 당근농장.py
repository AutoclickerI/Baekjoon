N,R,C=map(int,input().split())
f=R+C&1
exec("print(('v.'*99)[f:f+N]);f^=1;"*N)