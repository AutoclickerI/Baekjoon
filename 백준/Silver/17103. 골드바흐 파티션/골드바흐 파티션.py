l=[*range(10**6)]

for i in range(2,10**6):
    if l[i]:
        tmp = 2*i
        while tmp<10**6:
            l[tmp] = 0
            tmp += i

primes = [i for i in l[2:]if i]
def partition(n):
    ans=ptr1=0
    ptr2=78497
    while ptr2-ptr1+1:
        val=primes[ptr1]+primes[ptr2]
        ans+=val==n
        if val<n:ptr1+=1
        else:ptr2-=1
    return ans
for _ in[0]*int(input()):
    print(partition(int(input())))