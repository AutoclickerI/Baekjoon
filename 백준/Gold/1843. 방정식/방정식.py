N=int(input())
k=N+1>>1

print((k-1)*k-N%2*~-N//2)

s=set()
for i in range(1,N//2+1):
    if N%i<1:
        s|={i,N//i}

ss=sorted(s)
ls=len(s)
ans=0
for i in range(ls):
    for j in range(i,ls):
        if ss[i]+ss[j]in s:
            ans+=1
print(ans)

*is_prime,=range(N+1)
for i in range(2,N):
    if is_prime[i]:
        is_prime[2*i::i]=[0]*len(range(2*i,N+1,i))
primes=[i for i in is_prime if 1<i]

print(sum(j-i==2 for i,j in zip(primes,primes[1:])))