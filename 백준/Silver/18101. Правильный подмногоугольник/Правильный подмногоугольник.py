N=int(input())
i=3
if N%3==0:print(3)
elif N%4==0:print(4)
else:
    N>>=~N%2
    while i*i<=N>0<N%i:i+=2
    print(N*(i*i>N)or i)