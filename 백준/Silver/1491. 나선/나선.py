N,M=map(int,input().split())
p,q=sorted([N, M])
print(*[[s:=p+1>>1,q-s][p%2],s-1][::p%2*2*(M<N)-1])