N,P=map(int,input().split())
f=P<N*2
for i in range(*(a:=1,N+1,P)[f:f+2]):a=a*i%P
print(f*pow(-a,-1,P)or a)