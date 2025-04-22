task=int(input())
N=int(input())

d={1:'do',
   2:'ke',
   3:'tur',
   4:'boi',
   5:'oro',
   6:'dare'}

p={0:'',
   1:'land',
   2:'tilej',
   3:'kzuen',
   4:'alkzuen'}

def to_7(n):
    s=0
    p=0
    while n:
        s+=n%7*10**p
        n//=7
        p+=1
    return s

if task==1:
    z=1
    n=to_7(N)
    l=[d[n%10]]if n%10 else[]
    n//=10
    while n:
        if n%10:
            l+=[d[n%10],''][n%10<2]+p[z],
        n//=10
        z+=1
    print(*l[::-1])
else:
    po={i*i for i in range(1,101)}
    *primes,=range(10001)
    primes[1]=0
    for i in range(2,10001):
        if primes[i]:
            primes[i*2::i]=[0]*len(range(2*i,10001,i))
    primes={i for i in primes if i}
    cnt=0
    polyi=set()
    for j in po:
        for i in primes:
            if i*j<=N:polyi|={i*j+k for k in range(105,N+1,105)if i*j+k<=N}
    print(len(polyi))