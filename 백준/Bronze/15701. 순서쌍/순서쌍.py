N=int(input())
c=0
for i in range(1,int(N**.5)+1):c+=(N%i<1)*(1+(i**2<N))
print(c)