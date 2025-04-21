N=int(input())

*primes,=range(N+1)

primes[1]=0

for i in range(2,N+1):
    if primes[i]:
        primes[2*i::i]=[0]*len(range(2*i,N+1,i))

p=[i for i in primes if i]

cnt=0
for i in p:cnt+=N%i<1

is_lee=3<N and N!=5 and sum(map(int,str(N)))%2
is_im=N in[2,4]or~cnt*(1<cnt)%2

if is_lee and is_im:print(4)
elif is_lee:print(1)
elif is_im:print(2)
else:print(3)