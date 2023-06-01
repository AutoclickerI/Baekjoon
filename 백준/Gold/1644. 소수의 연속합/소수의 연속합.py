l=[*range(4000099)]
l[1]=0
for i in range(4000099):
    if l[i]:
        j=2*i
        while j<4000099:
            l[j]=0
            j+=i
prime=[i for i in l if i]
primesum=[0]
for i in range(283154):
    primesum+=[primesum[-1]+prime[i]]
n=int(input())
ans=0
ptr1=0
ptr2=1
while ptr2-ptr1:
    if primesum[ptr2]-primesum[ptr1]<n:
        ptr2+=1
    else:
        ans+=(primesum[ptr2]-primesum[ptr1]==n)
        ptr1+=1
print(ans)